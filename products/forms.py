from .models import Product
from django import forms

class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title','content', 'price', 'discount'
        ]
        