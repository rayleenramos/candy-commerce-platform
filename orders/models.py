from django.db import models
from django.conf import settings
from store.models import Candy


class Order(models.Model):
    # represents a customer's final order (like a receipt).
    # who bought it, where to send it, and the current status.
    STATUS_CHOICES = (
        ("Created", "Created"),
        ("Shipped", "Shipped"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    )

    # Customer Information
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    
    # Order Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Created")
    
    # Link to the registered user (optional, so guest checkout could work in future)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        # Show newest orders first
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"

    def update_status_based_on_time(self):
        """
        Updates the order status based on time elapsed since creation.
        For demo purposes:
        0-1 min: Created
        1-2 min: Shipped
        2-3 min: Out for Delivery
        >3 min: Delivered
        """
        from django.utils import timezone
        
        now = timezone.now()
        diff = now - self.created_at
        minutes_passed = diff.total_seconds() / 60

        if minutes_passed >= 3:
            self.status = "Delivered"
        elif minutes_passed >= 2:
            self.status = "Out for Delivery"
        elif minutes_passed >= 1:
            self.status = "Shipped"
        
        self.save()

    def get_total_cost(self):
        # Calculates the total cost of all items in this order
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    # Represents a single line item in an order.
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Candy, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        # Calculates total price for this specific item
        return self.price * self.quantity
