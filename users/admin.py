from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Userprofile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'country']
    list_filter = ['firstname']
    
    