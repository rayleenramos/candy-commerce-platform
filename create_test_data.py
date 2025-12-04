import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "candystore.settings")
django.setup()

from django.contrib.auth.models import User
from store.models import Candy, Order, OrderItem


def create_test_data():
    # Create test user
    user, created = User.objects.get_or_create(username="testuser")
    if created:
        user.set_password("password123")
        user.save()
        print("Created testuser")
    else:
        print("User testuser already exists")

    # Create dummy candy if none exists
    candy, created = Candy.objects.get_or_create(
        name="Test Candy",
        defaults={
            "description": "Delicious test candy",
            "price": 1.99,
            "stock": 100,
            "category": "Test",
        },
    )

    # Create an order
    order = Order.objects.create(user=user, status="Created", total_price=5.97)

    OrderItem.objects.create(order=order, candy=candy, quantity=3, price=1.99)

    print(f"Created Order #{order.id} for {user.username}")


if __name__ == "__main__":
    create_test_data()
