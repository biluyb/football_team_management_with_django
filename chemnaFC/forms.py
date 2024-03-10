import re
from django import forms
from .models import Fans,FanPicture

# class FansForm(forms.ModelForm):
#     fan_picture=forms.FileField( null=True)
#     name = forms.CharField(max_length=100)
#     gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')), widget=forms.RadioSelect)
#     fan_level = forms.ChoiceField(choices=(('A', "level3"), ('B', "level2"), ('C', "Topfan")))
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

# class FansForm(forms.ModelForm):
#     class Meta:
#         model = Fans
#         fields = "__all__"
class FanForm(forms.ModelForm):
    class Meta:
        model= Fans
        fields="__all__"

class FansPictureForm(forms.ModelForm):
    class Meta:
        model=FanPicture
        fields="__all__"

        # labels ={
        #    "name":"Your Name",
        #    "email":"Your Email Address"
        # }
        # error_message={
        #     "name": {
        #         "required":"You Must Enter Your Name",
        #         "max_length":"Your Name is Too Long"
        #     }
        # }
        

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and len(password) < 8:
            self.add_error('password', 'Password must be at least 8 characters long.')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')

        if password and not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
            self.add_error('password', 'Password must contain both letters and numbers.')

        return cleaned_data