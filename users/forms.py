from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms  
from .models import Userprofile 
from django_countries.widgets import CountrySelectWidget

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        error_messages = {
            "username": {
                'required': 'Username must not be empty',
            },
            "email": {
                'required': 'Please provide an email',
            },
        }
        
        
    def clean_username(self):
        username = self.cleaned_data.get('username')   
         
        try:
            User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(f'Username {username} is already in use')
    
    def clean_email(self):   
        email = self.cleaned_data.get('email')
         
        try:
            User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email 
        raise forms.ValidationError(f'Email {email} is already in use')
        

class UserprofileForm(forms.ModelForm):
    
    class Meta:
        model = Userprofile
        exclude = ['user']
        
        widgets = {'country': CountrySelectWidget(attrs={'class': 'form-control', 'placeholder': 'Country'}, 
                                                  layout='{widget}<i class=""></i>'
                                                  )}
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
            
        try:
            User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(f'Email {email} is already in use')
        