from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # Form for customers to enter their shipping information during checkout
    card_number = forms.CharField(
        max_length=16,
        label="Card Number",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "1234 1234 1234 1234"}),
    )
    card_expiry = forms.CharField(
        max_length=5,
        label="Expiration Date (MM/YY)",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "MM / YY"}),
    )
    card_cvv = forms.CharField(
        max_length=3,
        label="CVV",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "CVC"}),
    )
    name_on_card = forms.CharField(max_length=100, label="Name on Card", required=True)
    country = forms.CharField(
        max_length=100, label="Country or Region", initial="United States"
    )
    save_card = forms.BooleanField(required=False, label="Save card")

    class Meta:
        model = Order
        fields = ["customer_name", "email", "address", "city", "zip_code"]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
        }
