from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Review, Category, About, SavedBookModel, Contact 
from django.db.models import Avg
from django.views.generic import View, TemplateView, ListView
from .forms import ReviewForm, ContactForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView 
from .filters import BookFilters
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.

def homepage(request):
    """
        This view contains the latest books in the store. 
        Therefore, it contains logic for accessing the latest books 
        from the database and then to the templates.
    """
    
    latest_books = Book.objects.filter().order_by('-id')[:3]
    book_count = latest_books.count()
    category = Category.objects.all()
    
    context = {
        'latest_books': latest_books,
        'book_count':book_count,
        'category_list': category,
    }
    
    return render(request, 'book_app/index.html', context)


def all_books(request):
    
    books = Book.objects.all().order_by('-rating')
    book_count = books.count()
    book_filter = BookFilters(request.GET, queryset=books)
    filtered_books = book_filter.qs 
    paginator = Paginator(books, 4)
    page = request.GET.get('page')
    paged_object = paginator.get_page(page)
    
    
    context = {
        'book_count': book_count,
        # 'book_filter': book_filter,
        'books': paged_object,
        'page': page,
        'books': filtered_books,
    }
    
    return render(request, 'book_app/all_books.html', context)




def book_details(request, slug):
    book_item = get_object_or_404(Book, slug=slug)
    author = book_item.author
    rating_range = range(book_item.rating)
    missed_rating = range(5 - book_item.rating) 
    related_books = Book.objects.exclude(slug=slug).filter(author=author)
    reviews = Review.objects.filter(book__slug=book_item.slug)
    is_saved = SavedBookModel.objects.filter(books__title=book_item.title, owner__username=request.user.username)
    review_form = ReviewForm()
    
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        
        if review_form.is_valid():
            book_review_form = review_form.save(commit=False)
            book_item = get_object_or_404(Book, slug=slug)
            book_review_form.book = book_item
            review_form.save()
            messages.success(request, "Your review has been sent successfully")
            return redirect("book-detail", slug=slug)
        
    else:
        review_form = ReviewForm()
        
    
    context = {
                'book': book_item, 
                'review_form': review_form, 
                'related_books': related_books,
                'rating_range': rating_range,
                'missed_rating': missed_rating,
                'reviews': reviews ,
                'is_saved': is_saved
            }
    
    return  render(request, 'book_app/book_detail.html', context)
    


def author_page(request, firstname, lastname, pk):
    specific_author = Author.objects.get(first_name=firstname, last_name=lastname, id=pk)
    books_by_author = specific_author.books.filter()
    book_filter = BookFilters(request.GET, queryset=books_by_author)
    books_by_author = book_filter.qs 
    paginator = Paginator(books_by_author, 4)
    page = request.GET.get('page')
    paged_category = paginator.get_page(page)
    
    context = {
        'specific_author': specific_author,
        'book_filter': book_filter,
        'page': page,
        'books_by_author': paged_category,
    }
    
    return render(request, 'book_app/author.html', context)


class CategoryView(TemplateView):
    template_name = "book_app/book_category.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = kwargs["title"] 
        category = Category.objects.get(title=title)
        book = Book.objects.filter(category=category)
        book_filter = BookFilters(self.request.GET, queryset=book)
        book = book_filter.qs 
        context["category"] = category 
        context["books_by_category"] = book
        context["book-filter"] = book_filter
          
        return context
    
    
class CategoryListView(ListView):
    model = Category
    template_name = "book_app/categories.html"
    context_object_name = "category_list"    
 

class AddToSavedBooksView(LoginRequiredMixin ,View):
    login_url = 'login-page'
    
    def get(self, request):
        saved_books = SavedBookModel.objects.filter(owner=request.user)
        paginator = Paginator(saved_books, 4)
        page = request.GET.get('page')
        paged_category = paginator.get_page(page)
        
        context = {
            'saved_books': saved_books,
            'page': page,
            'paged_category': paged_category,
        }
        
        return render(request, 'book_app/saved_book.html', context)
    
    def post(self, request):
        book_slug = request.POST.get('book_slug')
        book = Book.objects.get(slug=book_slug)
        saved_book = SavedBookModel.objects.filter(books__slug=book_slug, owner=request.user)
        
        if not saved_book:
            saved_book_item = SavedBookModel()
            saved_book_item.books = book 
            saved_book_item.owner = request.user 
            saved_book_item.save()
            messages.success(request, 'Book successfully added to Save later')
        else:
            saved_book.delete()
            messages.success(request, 'Book successfully removed from Save later')
            
        return redirect("book-detail", slug=book_slug)
    
class ContactFormView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "book_app/contactform.html"
    success_url = reverse_lazy('contact-form')
    success_message = "Message successfully sent!"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = About.objects.get(pk=1)
        context["about"] = about
         
        return context 