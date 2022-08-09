from django.urls import path 
from . import views 

urlpatterns = [
    path('book-detail/addtocart/', views.addtoshopcart, name='addtocart'),
    path('shopcart/', views.shopcart, name='shopcart'),
    path('updatequantity/<int:pk>/', views.update_item_quantity, name='updatequantity'),
    path('deletefromcart/<int:pk>/', views.deletefromcart, name='delete-item'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.paystack_payment, name='order'),
    path('ordercompleted/', views.order_completed, name='order-completed'),
    path('order-history/', views.order_history, name='order-history')
]
