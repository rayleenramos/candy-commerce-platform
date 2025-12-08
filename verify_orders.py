import os
import django
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "candystore.settings")
django.setup()

from django.contrib.auth import get_user_model
from store.models import Candy
from orders.models import Order
from django.test import Client

from django.conf import settings
settings.MIDDLEWARE = [m for m in settings.MIDDLEWARE if "csrf" not in m.lower()]
settings.ALLOWED_HOSTS = ["testserver", "localhost", "127.0.0.1"]

def verify_order_flow():
    print("=== Verifying Order Flow ===")
    
    # 1. Setup Data
    User = get_user_model()
    user, _ = User.objects.get_or_create(username="testuser", email="test@example.com")
    if not user.check_password("password"):
        user.set_password("password")
        user.save()
    
    candy, _ = Candy.objects.get_or_create(
        name="Test Candy",
        defaults={"price": Decimal("1.99"), "stock": 100, "description": "Test"}
    )
    
    # 2. Add to Cart (Session)
    client = Client()
    client.force_login(user)
    
    # Add item
    client.post(f"/cart/add/{candy.id}/", {"quantity": 2, "override": "False"})
    
    # 3. Checkout
    # First GET to populate cookie
    print("Fetching checkout page...")
    client.get("/orders/create/")
    
    # Get token
    csrftoken = client.cookies.get('csrftoken')
    if csrftoken:
        token = csrftoken.value
    else:
        token = "" # Should fail if strict, but Client often passes anyway
                   # If fails, we know why.

    print("Submitting Order...")
    response = client.post("/orders/create/", {
        "customer_name": "Test User",
        "email": "test@example.com",
        "address": "123 Candy Lane",
        "city": "Sweet City",
        "zip_code": "12345",
        "csrfmiddlewaretoken": token
    }, follow=True)
    
    if response.status_code == 200:
        print("Checkout POST successful.")
        # Check if we are on the success page
        if "Thank You!" in response.content.decode():
             print("SUCCESS: Redirected to success page.")
        else:
             print("WARNING: 200 OK but 'Thank You' not found.")
    else:
        print(f"Checkout POST failed: {response.status_code}")
        
    # 4. Verify Database
    last_order = Order.objects.first()
    if last_order:
        print(f"Order Created: ID #{last_order.id}")
        items_count = last_order.items.count()
        print(f"Items: {items_count}")
        
        if items_count > 0:
            item = last_order.items.first()
            print(f"Item: {item.quantity}x {item.product.name}")
            
            # Verify user link
            if last_order.user != user:
                print(f"VERIFICATION FAILED: Order not linked to user. Expected {user}, got {last_order.user}")
            elif item.product == candy and item.quantity == 2:
                print("VERIFICATION PASSED: Order saved correctly and linked to user.")
            else:
                print("VERIFICATION FAILED: Item mismatch.")
        else:
            print("VERIFICATION FAILED: Order has no items.")
    else:
        print("FAILURE: No order found in database.")

if __name__ == "__main__":
    verify_order_flow()
