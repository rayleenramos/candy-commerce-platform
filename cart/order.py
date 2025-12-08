import uuid
from dataclasses import dataclass, field
from typing import List

# Models


@dataclass
class OrderItem:
    product_id: int
    product_name: str
    quantity: int
    price_per_unit: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.price_per_unit


@dataclass
class Order:
    customer_name: str
    items: List[OrderItem]
    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: str = "Created"  # initial status

    @property
    def total_amount(self) -> float:
        return sum(item.subtotal for item in self.items)


# Cart - Order Conversion


def create_order_from_cart(cart_items: List[dict], customer_name: str) -> Order:
    """
    cart_items: list of dicts like:
        {
          "product_id": 1,
          "product_name": "Apple",
          "quantity": 2,
          "price_per_unit": 0.99
        }
    """
    order_items = [
        OrderItem(
            product_id=item["product_id"],
            product_name=item["product_name"],
            quantity=item["quantity"],
            price_per_unit=item["price_per_unit"],
        )
        for item in cart_items
    ]

    order = Order(customer_name=customer_name, items=order_items)
    return order