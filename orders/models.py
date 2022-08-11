from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField 
from book_app.models import Book
# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    order_code = models.CharField(max_length=100)
    order_placed = models.BooleanField() 
    
    def __str__(self):
        return f"{self.book.title} added by {self.user.username}"
    # property that will be called in the template 
    @property 
    def amount(self):
        if self.book.id is not None:
            return float(self.quantity * self.book.price)
        else:
            return None 
        

class Payment(models.Model):
    STATUS =(
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    
    PLATFORM = (
        ('Paystack', 'Paystack'),
        ('Paypal', 'Paypal'),
    )
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total = models.FloatField(null=True, blank=True)
    order_placed = models.BooleanField(default=False)
    order_code = models.CharField(max_length=100, editable=False)
    payment_code = models.CharField(max_length=100, editable=False)
    first_name = models.CharField(max_length=15)
    last_name= models.CharField(max_length=15)
    phone= models.CharField(blank=True, max_length=20)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(blank=True, max_length=20)
    country = CountryField(blank_label='select country', null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    adminnote = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_platform = models.CharField(max_length=20, null=True, choices=PLATFORM)
       
    
    def __str__(self):
        return f"{self.user.username} paid using {self.payment_platform}"
