from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your forms here.


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter username",
        "autocomplete": "off",
        "class": "register-field"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Enter email address",
        "autocomplete": "off",
        "class": "register-field"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password",
        "class": "register-field"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm password",
        "class": "register-field"
    }))
