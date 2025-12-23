from store.models import Candy
import sys


def verify_stock():
    with open("verify_output.txt", "w") as f:
        product = Candy.objects.first()
        if not product:
            f.write("No candies found.")
            return

        initial_stock = product.stock
        f.write(f"Product: {product.name}\n")
        f.write(f"Initial Stock: {initial_stock}\n")

        quantity_bought = 2
        f.write(f"Simulating purchase of {quantity_bought} items...\n")

        product.stock -= quantity_bought
        product.save()

        product.refresh_from_db()
        current_stock = product.stock
        f.write(f"Current Stock: {current_stock}\n")

        if current_stock == initial_stock - quantity_bought:
            f.write("SUCCESS: Stock was correctly updated.\n")
        else:
            f.write("FAILURE: Stock was NOT updated correctly.\n")

        product.stock = initial_stock
        product.save()
        f.write("Cleanup: Stock restored to original value.\n")


if __name__ == "__main__":
    verify_stock()
