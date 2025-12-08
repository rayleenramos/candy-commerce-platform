import uuid
from dataclasses import dataclass, field
from typing import List

# Simulated Checkout Flow


def review_cart(cart_items: List[dict]) -> None:
    print("=== CART REVIEW ===")
    if not cart_items:
        print("Your cart is empty.\n")
        return

    for item in cart_items:
        line_total = item["quantity"] * item["price_per_unit"]
        print(
            f"- {item['product_name']} (x{item['quantity']}) "
            f"@ ${item['price_per_unit']:.2f} each = ${line_total:.2f}"
        )

    cart_total = sum(i["quantity"] * i["price_per_unit"] for i in cart_items)
    print(f"\nCart Total: ${cart_total:.2f}\n")


def display_order_confirmation(order: Order) -> None:
    print("\n=== ORDER CONFIRMATION ===")
    print(f"Order ID: {order.order_id}")
    print(f"Customer: {order.customer_name}")
    print(f"Status: {order.status}\n")

    for item in order.items:
        print(f"- {item.product_name} (x{item.quantity}) " f"= ${item.subtotal:.2f}")

    print(f"\nOrder Total: ${order.total_amount:.2f}")
    print("Thank you for your order!")


def checkout(cart_items: List[dict], customer_name: str) -> None:
    # 1. Review cart
    review_cart(cart_items)

    if not cart_items:
        print("Cannot proceed to checkout with an empty cart.")
        return

    # 2. Simulate user confirmation
    confirm = input("Proceed to place order? (y/n): ").strip().lower()
    if confirm != "y":
        print("Checkout cancelled.")
        return

    # 3. Convert cart to order
    order = create_order_from_cart(cart_items, customer_name)

    # 4. Display order confirmation
    display_order_confirmation(order)


# Example usage

if __name__ == "__main__":
    # Simulated cart data
    cart = [
        {
            "product_id": 1,
            "product_name": "Apple",
            "quantity": 3,
            "price_per_unit": 0.99,
        },
        {
            "product_id": 2,
            "product_name": "Bread",
            "quantity": 1,
            "price_per_unit": 2.49,
        },
    ]

    checkout(cart, customer_name=" ")
