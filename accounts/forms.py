from django import forms
from .models import SavedCard


class SavedCardForm(forms.ModelForm):
    card_number = forms.CharField(
        max_length=16,
        label="Card Number",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "1234 1234 1234 1234"}),
    )
    expiry_date = forms.CharField(
        max_length=5,
        label="Expiry Date (MM/YY)",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "MM / YY"}),
    )
    card_holder_name = forms.CharField(
        max_length=100, label="Name on Card", required=True
    )
    cvv = forms.CharField(
        max_length=4,
        label="CVC",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "CVC"}),
    )

    class Meta:
        model = SavedCard
        fields = ["card_holder_name", "card_number", "expiry_date"]


from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = (
                "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
            )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = (
                "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
            )

    class Meta:
        model = Profile
        fields = ["phone_number"]
