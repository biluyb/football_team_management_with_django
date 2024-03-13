import re
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import FanForm,FansPictureForm,LoginForm
from .models import Squad, Matches,Table,Fans,FanPicture
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView,CreateView
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request , "chemnaFC/index.html")

def squad(request):
    squad = Squad.objects.all()
    return render(request , "chemnaFC/squad.html",{"squad":squad})

def table(request):
    table=Table.objects.all()
    sorted_entries = sorted(table, key=lambda x: (x.point, x.goal), reverse=True)
    return render(request , "chemnaFC/table.html", {"table":sorted_entries})

def match(request):
    match = Matches.objects.all()
    return render(request , "chemnaFC/match.html", {"match":match})

def players_information(request, player):
    # detail =Squad.objects.get(pname=player)
    # return render(request , "chemnaFC/players_detail.html", {"detail":detail})
    detail = get_object_or_404(Squad, pname=player)
    return render(request, "chemnaFC/players_detail.html", {"detail": detail})

# def fan(request):
#     if request.method == 'POST':
#       form = FansForm(request.POST)
#       if form.is_valid():
#                 fan_save = Fans(
#                 name=form.cleaned_data['name'],
#                 gender=form.cleaned_data['gender'],
#                 fan_level=form.cleaned_data['fan_level'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password']
#                     )
#                 fan_save.save()
#                 return HttpResponseRedirect("/thankyou")   
#     else : 
#      form = FansForm()
#     return render(request, "chemnaFC/fan.html",{"form":form})
# class FansFormViews(View):
#     def get(self,request):
#         form = FansForm()
#         return render(request, "chemnaFC/fan.html",{"form":form})
#     def post(self,request):
#         form = FansForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thankyou")
#         return render(request,"chemnaFC/fan.html",{"form":form})
# # class FansFormViews(FormView):
class FansFormViews(CreateView):
    template_name="chemnaFC/fan.html"
    model=Fans
    form_class=FanForm
    success_url="/thankyou"

    def form_valid(self, form):
        # Additional validation in the view
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']

        if len(password) < 8:
            form.add_error('password', 'Password must be at least 8 characters long.')

        if password != confirm_password:
            form.add_error('confirm_password', 'Passwords do not match.')

        if not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
            form.add_error('password', 'Password must contain both letters and numbers.')

        if form.errors:
            return self.form_invalid(form)

        return super().form_valid(form)
    
class FanPictureView(CreateView):
    template_name="chemnaFC/fan.html"
    model=FanPicture
    fields="__all__"
    success_url="/thankyou"
class PictureView(ListView):
    template_name="chemnaFC/pictureview.html"
    model=FanPicture
    context_object_name="fan_picture"

# class MatchesVIew(CreateView):
#      template_name="chemnaFC/matchesform.html"
#      model=Matches
#      form_class=MatchesForm
#      success_url="/thankyou"
class ThankyouView(TemplateView):
    template_name= "chemnaFC/thankyou.html"
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["message"] = "thank you for register"
        return context
class FansListView(ListView):
    template_name="chemnaFC/fan_list.html"
    model=Fans
    context_object_name= "fan_list"

    # def get_queryset(self) :
    #     base_query=super().get_queryset()
    #     data=base_query.filter(fan_level='A' and 'C')
    #     return data
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     fan  = Fans.objects.all()
    #     context["fan_list"]=fan
    #     return context
class SingleFanView(DetailView):
    template_name="chemnaFC/single_fan.html"
    model=Fans
    context_object_name="single_fan"

    def get_context_data(self, **kwargs: Any) :
        context= super().get_context_data(**kwargs)
        loaded_page=self.object
        request=self.request
        favorite_id=request.session.get("favorite_ses")
        context["is_favorite"]=favorite_id==str(loaded_page.id)
        return context
class FavoriteView(View):
      def post(self,request):
          favorite_id=request.POST["favorite_input"]
          request.session["favorite_ses"]=favorite_id
          return HttpResponseRedirect("/fan_list/" + favorite_id)
      
# def login(request):
    # if request.method =="POST":
    #     name =request.POST.get("name")
    #     password=request.POST.get("password")
    #     user=auth.authenticate(username=name,password=password)
    #     if user is not None:
    #         auth.login(request, user)
    #         return render(request,"chemnaFC/fan_list.html")
    #     else:
    #         messages.error(request,'invalid information')

    # return render (request,"chemnaFC/login.html",{'form':LoginForm})
      
@login_required    
def ProfileView(request):
      

      return render (request,"chemnaFC/pictureview.html",{'section':'ProfileView'})



def forgot(request):
    return render (request,"chemnaFC/forgot.html")