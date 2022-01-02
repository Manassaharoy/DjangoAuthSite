from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields
from App_login import models
from App_login.models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="",
    widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True, label="",
    widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(required=True, label="",
    widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True, label="",
    widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation'}))
    
    class Meta:
        model = User
        fields = ('email','username','password1','password2')
    
    

class LoginUser(AuthenticationForm):
    username = forms.CharField(required=True, label="",
    widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(required=True, label="",
    widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ('username','password')
    
class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile
        exclude = ('user',)
    