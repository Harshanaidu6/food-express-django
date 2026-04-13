from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    
    address=models.CharField(max_length=200)
    image = models.ImageField(upload_to='restaurant_images/', null=True, blank=True)
    def __str__(self):
        return self.name
    


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, default="COD")

    def __str__(self):
        return self.user.username
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_address = models.TextField()

    def __str__(self):
        return self.full_address
    


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)  # pending, success, failed
    created_at = models.DateTimeField(auto_now_add=True)