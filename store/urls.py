"""
URLs for store app
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("candy/<int:candy_id>/", views.candy_detail, name="candy_detail"),
]
