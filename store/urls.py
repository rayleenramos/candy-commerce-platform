"""
URLs for store app
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("candy/<int:candy_id>/", views.candy_detail, name="candy_detail"),
    path("inventory/", views.inventory_list, name="inventory_list"),
    path("inventory/update/<int:candy_id>/", views.update_stock, name="update_stock"),
]
