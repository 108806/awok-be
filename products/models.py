from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True, null=True, max_length=256)
    price  = models.DecimalField(max_digits=15, 
        decimal_places=2,default=99.99)
    
    @property
    def sale_price(self):
        return float(self.price)

    def get_discount(self):
        return f'{self.sale_price*0.8:.2F}'

class API_User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    