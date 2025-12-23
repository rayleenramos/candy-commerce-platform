from django.contrib import admin
from .models import Profile, SavedCard


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number")
    search_fields = ("user__username", "user__email", "phone_number")


@admin.register(SavedCard)
class SavedCardAdmin(admin.ModelAdmin):
    list_display = ("user", "card_holder_name", "card_number", "expiry_date")
    list_filter = ("user",)
    search_fields = ("user__username", "card_holder_name")
