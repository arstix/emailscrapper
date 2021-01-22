from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from django.contrib.auth import get_user_model
from .models import *

class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'type':'password', 'align':'center', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'type':'password', 'align':'center', 'placeholder':'Confirm Password'}),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        widgets = {
            'username': TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Username'}),
            'first_name': TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Last Name'}),
            'email': EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email Address'}),
        }

        fields = ['username', 'first_name', 'last_name', 'email']
