from django.contrib import admin
from book_app.models import *
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author' ,'rating', 'is_bestselling']
    readonly_fields = ('slug',)
    list_filter = ['author' ,'rating', 'is_bestselling',]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['first_name', 'last_name']
    
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'postal_code','city', 'country']
    list_filter = ['country']
    
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    list_filter = ['name']
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'rating']
    list_filter = ['fullname']
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['about_text']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    
@admin.register(SavedBookModel)
class SavedBookModelAdmin(admin.ModelAdmin):
    list_display = ['owner']