from django.http import HttpResponse
from django.shortcuts import redirect, render
from .import views

def unauthenticated_user(view_func):
    def wrapper_func(request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def not_fan(view_func):
    def wrapper_func(request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect("/fan_list")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func
