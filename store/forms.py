from django import forms
from .models import Candy


class CandyForm(forms.ModelForm):
    class Meta:
        model = Candy
        fields = ["name", "description", "price", "stock", "category", "image_url"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input-field"}),
            "description": forms.Textarea(attrs={"class": "input-field", "rows": 3}),
            "price": forms.NumberInput(attrs={"class": "input-field"}),
            "stock": forms.NumberInput(attrs={"class": "input-field"}),
            "category": forms.TextInput(attrs={"class": "input-field"}),
            "image_url": forms.URLInput(attrs={"class": "input-field"}),
        }
