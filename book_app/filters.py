import django_filters 
from .models import Book 

class BookFilters(django_filters.FilterSet):
    
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    
    class Meta:
        model = Book 
        fields = ['title']