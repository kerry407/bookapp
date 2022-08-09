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
            email = register_form.cleaned_data.get('email')
            messages.success(request,  f'Account for {email} has been created')
            
            return redirect('login-page')
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
        username = request.POST.get('username')
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
    payments = Payment.objects.filter(user__username=request.user.username, order_placed=True).order_by('-id')
    reference_array = [item.order_code for item in payments]
    
    cart = ShopCart.objects.filter(user__username=request.user.username, order_code__in=reference_array, order_placed=True)
    
    context = {
        'userprofile': profile,
        'payments': payments,
        'cart': cart,
    }
    return render(request, 'users/userprofile.html', context)
    