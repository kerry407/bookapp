from django.shortcuts import render, redirect
from book_app.models import Book
from users.models import Userprofile 
from .models import Payment, ShopCart
import uuid
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_POST
import random 
import string 
import requests 
from django.contrib import messages 
import json 
from django.conf import settings 

# Create your views here.

@require_POST
@login_required(login_url="login-page")
def addtoshopcart(request):
    book_slug = request.POST["book_slug"]
    thequantity = request.POST.get("quantity")
    book_item = Book.objects.get(slug=book_slug)

    cart = ShopCart.objects.filter(user__username=request.user.username, book= book_item, order_placed=False)
    
    if cart:
        book_check = ShopCart.objects.filter(user=request.user, book=book_item, order_placed=False).first()
        
        if book_check:
            book_check.quantity += int(thequantity)
            book_check.save()
        
        else:
            book_cart = ShopCart()
            book_cart.quantity = thequantity
            book_cart.user = request.user 
            book_cart.book = book_item
            book_cart.order_placed = False 
            book_cart.order_code = cart[0].order_code 
            book_cart.save()
            
    else:
        ordercode = str(uuid.uuid4())
        new_cart = ShopCart()
        new_cart.quantity = thequantity
        new_cart.user = request.user 
        new_cart.book = book_item
        new_cart.order_placed = False 
        new_cart.order_code = ordercode
        new_cart.save()
        
    messages.success(request, "Item successfully added to cart")
    
    return redirect("book-detail", slug=book_slug)


@login_required(login_url="login-page")
def shopcart(request):
    cart = ShopCart.objects.filter(user=request.user, order_placed=False)
    SUBTOTAL = 0
    SHIPPING_FEE = 0
   
    
    for item in cart:
        SUBTOTAL += item.book.price * item.quantity
    
    if SUBTOTAL > 100:
        SHIPPING_FEE = round(0.08 * SUBTOTAL, 2)
    else:
        SHIPPING_FEE = 0
        
    VAT = round(0.075 * SUBTOTAL, 2)
    TOTAL = SUBTOTAL + SHIPPING_FEE + VAT
    
    context = {
        'cart': cart,
        'subtotal': SUBTOTAL,
        'vat': VAT,
        'shipping_fee': SHIPPING_FEE,
        'total': TOTAL
    }
     
    return render(request, "orders/shopcart.html", context)

@require_POST
@login_required(login_url="login-page")
def update_item_quantity(request, pk):
    new_quantity = request.POST.get("newquantity")
    book_item = ShopCart.objects.get(id=pk)
    
    # Update the item quantity
    book_item.quantity = new_quantity
    book_item.save()
    messages.success(request, 'Item quantity successfully updated')
    return redirect("shopcart")
    
    
@login_required(login_url="login-page")
def deletefromcart(request, pk):
    url = request.META.get('HTTP_REFERER')
    ShopCart.objects.get(id=pk).delete()
    messages.success(request, 'Item successfully removed from cart')
    return redirect(url)

# helper function to convert $ price to Naira
def convert_to_naira(amount):
    return amount * 600
        
         
def checkout(request):
    cart = ShopCart.objects.filter(user=request.user, order_placed=False)
    get_profile = Userprofile.objects.get(user__username=request.user.username)
    order_code = None 
    SUBTOTAL = 0
    SHIPPING_FEE = 0
    
   
    
    for item in cart:
        SUBTOTAL += item.book.price * item.quantity
        order_code = item.order_code
        
    if SUBTOTAL > 100:
        SHIPPING_FEE = round(0.08 * SUBTOTAL, 2)
    else:
        SHIPPING_FEE = 0
        
    VAT = round(0.075 * SUBTOTAL, 2)
    TOTAL = SUBTOTAL + SHIPPING_FEE + VAT
    
    context = {
        'cart': cart,
        'subtotal': SUBTOTAL,
        'vat': VAT,
        'shipping_fee': SHIPPING_FEE,
        'total': TOTAL,
        'naira_total': convert_to_naira(TOTAL),
        'get_profile': get_profile,
        'order_code': order_code 
    }
    
    return render(request, 'orders/checkout.html', context)


@require_POST
@login_required(login_url='login-page') 
def paystack_payment(request):
    url = 'https://api.paystack.co/transaction/initialize'
    api_key = settings.API_KEY
    ordercode = request.POST.get('ordernumber')
    autogen_ref = ''.join(random.choices((string.digits + string.ascii_letters), k=12))
    profile = Userprofile.objects.get(user__username=request.user.username)
    total_amount = float(request.POST.get('total')) * 100 * 600
    callback_url = 'http://127.0.0.1:8000/orders/ordercompleted/'
    
    headers = {
        'Authorization': f"Bearer {api_key}"
    }
    
    order_data = {
        'email': profile.user.email,
        'amount': int(total_amount),
        'ref': autogen_ref,
        'callback_url': callback_url,
        'order_number': ordercode
    }
    
    try:
        response = requests.post(url, headers=headers, json=order_data)
    except requests.exceptions.RequestException:
        messages.error(request, f"Error while perfoming operation, please check your internet connection and try again!")
    else:
        transback = json.loads(response.text)
        rd_url = transback['data']['authorization_url']
        # create the order details
        order = Payment()
        order.user = request.user 
        order.first_name = profile.user.first_name   
        order.last_name = profile.user.last_name
        order.phone = profile.phone1
        order.payment_code = autogen_ref
        order.address = profile.address
        order.city = profile.city
        order.country = profile.country
        order.order_code = ordercode      
        order.order_placed = True 
        order.total = total_amount/(100 * 600)
        order.save()
        return redirect(rd_url)
    return redirect('checkout')
        
        
@login_required(login_url='login-page')    
def order_completed(request):
    cart = ShopCart.objects.filter(user__username=request.user.username)
    profile = Userprofile.objects.get(user__username=request.user.username)
    
    for item in cart:
        item.order_placed = True 
        item.save()
        
        book = Book.objects.get(id=item.book.id)
        book.quantity_instock -= item.quantity 
        
        book.save()
        
    context = {
        'cart': cart,
        'profile': profile,
    }
    
    return render(request, 'orders/orderplaced.html', context)
        
def order_history(request):
    payments = Payment.objects.filter(user__username=request.user.username, order_placed=True).order_by('-id')
    
    context = {
        'payments': payments,
    }
    
    return render(request, 'orders/orderhistory.html', context)


