from django.contrib import admin
from .models import *   
# Register your models here.

@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ["id", "book", "user", "quantity", "order_code", "order_placed"]
    list_display_links = ["id"]
    list_filter = ["book", "user", "quantity", "order_code", "order_placed"]
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'order_placed', 'last_name', 'order_code', 'payment_code']
    list_display_links = ['first_name']