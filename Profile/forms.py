from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UpdateProfile(forms.ModelForm):


    class Meta:
        model =Profile
        fields =['job','facebook','telegram','bio']


class UpdateProfile2(forms.Form):
    username = forms.CharField(max_length=20)
    email =forms.EmailField(max_length=25)

class UdatePhoto(forms.ModelForm):
    class Meta:
        model =Profile
        fields =['profile_pic']

class DeleteForm(forms.Form):
    password =forms.CharField(widget=forms.PasswordInput())
