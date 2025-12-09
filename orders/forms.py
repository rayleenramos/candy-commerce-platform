from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # Form for customers to enter their shipping information during checkout
    class Meta:
        model = Order
        fields = ["customer_name", "email", "address", "city", "zip_code"]
