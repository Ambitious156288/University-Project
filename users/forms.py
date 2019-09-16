from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    imię = forms.CharField(max_length=100)
    nazwisko = forms.CharField(max_length=100)
    email = forms.EmailField()#required=false
    
    
    class Meta:
        model = User
        fields = ['username', 'imię', 'nazwisko', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    imię = forms.CharField(max_length=100)
    nazwisko = forms.CharField(max_length=100)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'imię', 'nazwisko', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['uczelnia', 'wydział', 'rok', 'image']