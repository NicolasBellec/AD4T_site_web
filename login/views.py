from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from home.views import home

# Create your views here.
def connectView(request):
    error = False

    if request.method == "POST":
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes

            if user:  # Si l'objet renvoyé n'est pas None
                login(request=request, user=user)  # nous connectons l'utilisateur
                return redirect(home)

            else: # sinon une erreur sera affichée
                error = True

    else:
        form = forms.LoginForm()


    return render(request, 'login.html', locals())

def disconnectView(request):
    logout(request)
    return redirect(home)
