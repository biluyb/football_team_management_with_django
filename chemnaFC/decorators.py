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

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("you are not allowed to see this page")
            
        return wrapper_func
        
    return decorator
 