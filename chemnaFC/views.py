import re
from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AdressForm, ClubsForm, FanForm, MatchForm, PositionForm,RegisterForm, SquadForm, TableForm
from .models import Adress, Position, Squad, Matches,Table,Fans,FanPicture,Clubs

from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth import  authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import unauthenticated_user,not_fan
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

@login_required(login_url='/login')
def ticket(request):
    return render(request , "chemnaFC/ticket.html")

@not_fan
def fanPage(request):
    return render(request , "chemnaFC/fanPage.html")

def players_information(request, player):
    detail = get_object_or_404(Squad, pname=player)
    return render(request, "chemnaFC/players_detail.html", {"detail": detail})
@method_decorator(login_required(login_url='/login'),name='dispatch')
class FansFormViews(CreateView):
    template_name="chemnaFC/fan.html"
    model=Fans
    form_class=FanForm
    success_url="/thankyou"

    def form_valid(self, form):
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
# @unauthenticated_user    
def signup(request):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "account was created for " + user)
            return HttpResponseRedirect("/login")
        else:
            form = RegisterForm()
        return render (request,"chemnaFC/register.html",{"form":form})

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request,user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect("/")
        else:
            messages.info(request,'"incorrect username or password"')
    context = {}
    return render (request,"chemnaFC/login.html",context)

def logoutPage(request):
    logout(request)
    return redirect('login_page')
      
def forgot(request):
    return render (request,"chemnaFC/forgot.html") 

def admin_dashboard(request):
    match_form = MatchForm(request.POST or None)
    position_form = PositionForm(request.POST or None)
    squad_form = SquadForm(request.POST or None)
    table_form = TableForm(request.POST or None)
    address_form = AdressForm(request.POST or None)
    clubs_form = ClubsForm(request.POST or None)

    forms = {
        'Match Form': match_form,
        'Position Form': position_form,
        'Squad Form': squad_form,
        'Table Form': table_form,
        'Address Form': address_form,
        'Clubs Form': clubs_form,
    }

    if request.method == 'POST':
        for name, form in forms.items():
            if form.is_valid():
                form.save()
        return redirect('/dashboard')
    return render(request, 'chemnaFC/dashBoard.html', {'forms': forms})