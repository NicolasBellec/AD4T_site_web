from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class SubscribeForm(forms.Form):
    name = forms.CharField(label="Prénom", max_length=30)
    lastname = forms.CharField(label="Nom", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=form.PasswordInput)
    email = forms.EmailField(label="E-mail", label_suffix="", max_length=60)
