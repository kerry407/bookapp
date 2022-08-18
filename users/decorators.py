from django.shortcuts import redirect
from django.contrib import messages 


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, "Http request not allowed")
            return redirect('book-home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func