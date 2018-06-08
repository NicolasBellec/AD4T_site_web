from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class SubscribeForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=2048)
    last_name = forms.CharField(label="Nom", max_length=2048)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    email = forms.EmailField(label="Adresse e-mail")
