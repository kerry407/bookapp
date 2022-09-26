from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User 

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name_plural = 'Countries'

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code =  models.CharField(max_length=6)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.country} Postal Code: {self.postal_code}"
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    about = models.TextField(null=True)
    
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.get_fullname()
    
class Category(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to="images")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Book(models.Model):
    
    AVAILABLE = (
        ('In Stock','In Stock'),
        ('Out of Stock','Out of Stock'),
        ('Restocked','Restocked'),
    )
    
    """
    In the slugfield, using the db_index makes it very easy and 
    fast to lookup or search for data in that field. Bu only set db_index 
    to fields you would use most often because setting db_index to every
    field makes it slower because of load.
    """
    title = models.CharField(max_length=70)
    rating = models.IntegerField(
                    validators=[MinValueValidator(1),
                                MaxValueValidator(5)
                                ])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="books", blank=True)
    is_bestselling = models.BooleanField(default=False)
    published_countries = models.ManyToManyField(Country, blank=True)
    length = models.IntegerField(null=True, blank=True)
    read_time = models.CharField(max_length=15, null=True, blank=True)
    release_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    editors_note = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    isbn = models.CharField(max_length=100, null=True)
    slug = models.SlugField(default='', null=False, db_index=True, editable=False)
    book_image = models.ImageField(upload_to='images', default='static/images/about-img.png')
    price = models.FloatField(null=True, blank=True)
    available = models.CharField(max_length=30,blank=True, null=True, choices=AVAILABLE)
    minquantity = models.IntegerField(blank=True, null=True, default=1)
    quantity_instock = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1),
                                MaxValueValidator(100)
                                ])
    amount = models.IntegerField(blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        return f"Title: {self.title},  Author: {self.author}"

class Review(models.Model):
    fullname = models.CharField(max_length=70)
    review_message = models.TextField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                MaxValueValidator(5)
                                ])
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, related_name="books")
    date_created = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"A review was sent by {self.fullname}"
    
     
class About(models.Model):
    about_text = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "About"
    
class SavedBookModel(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="savedbook", null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.owner.username 
    

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=200)
    
    def __str__(self):
        return f"{self.fullname} sent a message with subject '{self.subject}'"
    
    
