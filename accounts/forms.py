from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username= forms.CharField(label="",max_length=120,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}))
    first_name = forms.CharField(label="",max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your first name'}))
    last_name = forms.CharField(label="",max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your last name'}))
    password1 = forms.CharField(label="",max_length=120,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    password2 = forms.CharField(label="",max_length=120,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm your password'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="",widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)























