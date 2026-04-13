from django.contrib import admin

# Register your models here.
from .models import Restaurant, MenuItem, Cart, Order
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Order)