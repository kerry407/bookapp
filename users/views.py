import email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from users.models import Userprofile
from .forms import RegisterForm, UserprofileForm
from django.contrib import messages 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from orders.models import Payment, ShopCart
# Create your views here.

        
@unauthenticated_user
def register_user(request):
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f"Account created successfully")
            return redirect('book-home')
        else:
            messages.error(request, register_form.errors)
    else:
        register_form = RegisterForm()
    
    context = {
        'register_form': register_form
    }
    
    return render(request, 'users/register.html', context)
    

@unauthenticated_user
def login_func(request):
    if request.method == "POST":
        
        try:
            email = request.POST.get('email')
            request_user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, f"No user with the email")
        else:
            username = request_user.username 
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
        
            if user:
                login(request, user)
                
                return redirect('book-home')
            else:
                messages.error(request, 'Username or password is not correct')
    
    return render(request, 'users/login.html')


@login_required(login_url='login-page')
def logout_view(request):
    logout(request)
    
    return redirect('book-home')
    

@login_required(login_url='login-page')
def userprofile_update(request):
    profile = Userprofile.objects.get(user__username=request.user.username)
    
    if request.method == "POST":
        profileform = UserprofileForm(request.POST, instance=request.user.userprofile)
        
        if profileform.is_valid():
            
            user_object = User.objects.get(username=request.user.username)
            user_object.first_name = request.POST.get("firstname") 
            user_object.last_name = request.POST.get("lastname") 
            user_object.email = request.POST.get("email") 
            user_object.save()
            
            profileform.save()
            messages.success(request, "Profile successfully updated")
            return redirect("user-profile")  
    else:
        profileform = UserprofileForm() 
    
    context = {
        'profileform': profileform,
        'userprofile': profile,
    }  
    
    return render(request, 'users/userupdate.html', context)

    
@login_required(login_url='login-page')
def userprofile(request):
    profile = Userprofile.objects.get(user__username=request.user.username)
    
    context = {
        'userprofile': profile,
    }
    return render(request, 'users/userprofile.html', context)
    