
from django.shortcuts import render
from orders.models import ShopCart    


def cartcounter(request):
    cart = ShopCart.objects.filter(user__username=request.user.username, order_placed=False)

    total_items = sum(item.quantity for item in cart)
        
    context = {
        'item_count': total_items
    }
    
    return context 


