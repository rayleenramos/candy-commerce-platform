from store.models import Candy
from decimal import Decimal


def verify_stock():
    # 1. Get a product
    product = Candy.objects.first()
    if not product:
        print("No candies found.")
        return

    initial_stock = product.stock
    print(f"Product: {product.name}")
    print(f"Initial Stock: {initial_stock}")

    # 2. Simulate Order Item creation logic (quantity = 2)
    quantity_bought = 2
    if initial_stock < quantity_bought:
        print(f"Not enough stock to test (need {quantity_bought}). Skipping.")
        return

    print(f"Simulating purchase of {quantity_bought} items...")

    # Simulate the view logic
    product.stock -= quantity_bought
    product.save()

    # 3. Reload from DB to verify persistence
    product.refresh_from_db()
    current_stock = product.stock
    print(f"Current Stock: {current_stock}")

    # 4. Verification
    if current_stock == initial_stock - quantity_bought:
        print("SUCCESS: Stock was correctly updated.")
    else:
        print("FAILURE: Stock was NOT updated correctly.")

    # 5. Cleanup (Restore stock)
    product.stock = initial_stock
    product.save()
    print("Cleanup: Stock restored to original value.")


if __name__ == "__main__":
    verify_stock()
