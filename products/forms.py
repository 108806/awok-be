from .models import Product
from django import forms
from django.contrib.auth.models import User

class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title','content', 'price', 'discount'
        ]
        
class User(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "id", "first_name", "last_name", "username"
        ]