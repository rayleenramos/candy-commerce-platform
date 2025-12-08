from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    # URL for the checkout page /orders/create/
    path("create/", views.order_create, name="order_create"),
    
    # URL for the user's order history /orders/history/
    # URL for the user's order history /orders/history/
    path("history/", views.order_history, name="order_history"),

    # URL for individual order detail /orders/order/<id>/
    path("order/<int:order_id>/", views.order_detail, name="order_detail"),
]
