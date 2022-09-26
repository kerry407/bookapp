import django_filters 
from .models import Book 
from django.db.models import Q 

class BookFilters(django_filters.FilterSet):
    
    search_obj = django_filters.CharFilter(method="custom_filter")
    
    class Meta:
        model = Book 
        fields = ['search_obj']
        
    def custom_filter(self, queryset, name, value):
        queryset = Book.objects.filter(
                                        Q(title__icontains=value) | 
                                        Q(author__first_name__icontains=value) | 
                                        Q(author__last_name__icontains=value)  |
                                        Q(category__title__icontains=value)
                            )
        return queryset
        
        