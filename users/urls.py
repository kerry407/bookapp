from django.urls import path 
from . import views 

urlpatterns = [
    path('register/', views.register_user, name='register-page'),
    path('login/', views.login_func, name='login-page'),
    path('logout/', views.logout_view, name='logout'),
    path('profileupdate/', views.userprofile_update, name='update-profile'),
    path('userprofile/', views.userprofile, name='user-profile')
]
