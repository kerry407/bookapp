
from django.db import models
from django.contrib.auth.models import User 
from django_countries.fields import CountryField

# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, null=True,)
    lastname = models.CharField(max_length=30, null=True)
    email = models.EmailField(verbose_name='Email Address')
    phone1 = models.CharField(max_length=20, null=True, verbose_name='Mobile number')
    phone2 = models.CharField(max_length=20, null=True, verbose_name='Secondary phone number')
    address = models.CharField(max_length=200, null=True, verbose_name='Address')
    country = CountryField(blank_label='select country', null=True, verbose_name='Country')
    city = models.CharField(max_length=20, null=True, verbose_name='City')
    zip_code = models.CharField(max_length=10, null=True, verbose_name='Postal code')
    
    def __str__(self):
        return f"Userprofile for {self.user.username}"
    
    
    
    
