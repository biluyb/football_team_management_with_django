from django import forms
from .models import Fans,FanPicture,Matches,Table,Squad,Position,Clubs,Adress
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FanForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= Fans
        fields="__all__"

        labels ={
           "name":"Your Name",
           "email":"Your Email Address"
        }
        error_message={
            "name": {
                "required":"You Must Enter Your Name",
                "max_length":"Your Name is Too Long"
            }
        }
class FansPictureForm(forms.ModelForm):
    class Meta:
        model=FanPicture
        fields="__all__"
class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields =["username","email", "password1","password2"]
        # fields="__all__"


class MatchForm(forms.ModelForm):
    class Meta:
        model=Matches
        fields = "__all__"

class PositionForm(forms.ModelForm):
    class Meta:
        model=Position
        fields = "__all__"

class SquadForm(forms.ModelForm):
    class Meta:
        model=Squad
        fields = "__all__"

class TableForm(forms.ModelForm):
    class Meta:
        model=Table
        fields = "__all__"

class AdressForm(forms.ModelForm):
    class Meta:
        model=Adress
        fields = "__all__"

class ClubsForm(forms.ModelForm):
    class Meta:
        model=Clubs
        fields = "__all__" 

