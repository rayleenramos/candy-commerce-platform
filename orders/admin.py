from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    # Allows admin to see the list of items inside the Order page.
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Admin interface for managing customer orders.
    # Can filter by status (Created/Shipped) and date.
    list_display = [
        "id",
        "customer_name",
        "email",
        "city",
        "status",
        "created_at",
        "updated_at",
    ]
    list_filter = ["status", "created_at", "updated_at"]
    inlines = [OrderItemInline]
