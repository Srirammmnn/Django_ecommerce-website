from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django import forms

class SignupForm(UserCreationForm):
    username = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control pink-input ','placeholder':'username'}))
    email = forms.TextInput(attrs={'class':'form-control pink-input','placeholder':'email address'})

    first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control pink-input','placeholder':'firstname'}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control pink-input','placeholder':'lastname'}))
    password1 = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control pink-input ','placeholder':'password'}))
    password2 = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control pink-input ','placeholder':'password'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2')