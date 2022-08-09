from django import forms 
from .models import Review, Contact 


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ["fullname", "review_message", "rating"]
        
        label = {
            "fullname": "Full Name",
            "review_message": "Review Message",
            "rating": "Your rating",
        }
        
        error_messages = {
            "fullname": {
                "required": "Please provide a name",
                "max_length": "Please provide a shorter name, name must not be more than 70 characters"
            },
            "review_message": {
                "required": "You have to provide a review message if you must send a review about this book",
                "max_length": "Your review message must not be more than 200 characters"
            }
        }
        
        widgets = {
            "fullname": forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Name',}),
            "review_message": forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Review Message'}),
            "rating": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating', 'min': '1', 'max': '5', 'id': 'rating'}),
        }

        

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"
        
        error_messages = {
            "fullname": {
                'required': 'Name must not be empty',
                'max_length': 'username cannot exceed 100 characters!'
            },
            "email": {
                'required': 'Email field must not be empty',
            },
            "subject": {
                'max_length': 'subject cannot exceed 20 characters!'
            },
            "message": {
                'required': 'This field cannot be empty!'
            }
        }
        
        widgets = {
            "fullname": forms.TextInput(attrs={'class': 'form-input', 'placeholder':'Your Name'}),
            "email": forms.EmailInput(attrs={'class': 'form-input', 'placeholder':'Email Address'}),
            "subject": forms.TextInput(attrs={'class': 'form-input', 'placeholder':'Subject'}),
            "message": forms.Textarea(attrs={'class': 'message-box', 'placeholder':'Place a message'})
        }
        
        
