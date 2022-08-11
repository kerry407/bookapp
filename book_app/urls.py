from django.urls import path 
from . import views  


urlpatterns = [
    path('', views.homepage, name='book-home'),
    path('all-books/', views.all_books, name='all-books'),
    path('saved-books/', views.AddToSavedBooksView.as_view(), name='save-book'),
    path('book-detail/<slug:slug>/', views.book_details, name='book-detail'),
    path('<str:firstname>-<str:lastname>/<int:pk>/', views.author_page, name='author-page'),
    path('category/<str:title>/', views.CategoryView.as_view(), name='category-page'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('contactform/', views.ContactFormView.as_view(), name='contact-form'),
]
