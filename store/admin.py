"""
Admin configuration for store app
"""

from django.contrib import admin
from .models import Candy


@admin.register(Candy)
class CandyAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock")
    list_filter = ("category",)
    search_fields = ("name", "description")
