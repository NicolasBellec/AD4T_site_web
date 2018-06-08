import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages import add_message, INFO, ERROR
from django.db.models import Q
from . import forms
from home.views import home

# Create your views here.
def connectView(request):
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
                add_message(request, ERROR, "Mauvais mot de passe ou nom d'utilisateur.")
                form = forms.LoginForm()
        else:
            add_message(request, INFO, "Erreur lors du traitement du formulaire.")
            form = forms.LoginForm()

    else:
        form = forms.LoginForm()


    return render(request, 'login.html', { 'form' : form })

def disconnectView(request):
    logout(request)
    return redirect(home)

def userPayment(request, user):
    context = {}

    return_url = 'https://'+DOMAIN+'login/validation'
    cancel_url = 'https://'+DOMAIN+'login/cancellation'

    r_token = requests.post('https://api.sandbox.paypal.com/v1/oauth2/token',
                       headers={'Accept':'application/json',
                                'Accept-Language':'FR'},
                       auth=('XXXX','XXXX'), #TO DEFINE
                       data={'grant_type':'client_credentials'})

    if r_token.status_code !=  200:
        add_message(request, INFO, "Erreur lors de la récupération du token paypal.\nContactez nous à l'adresse suivante : XXXX.")
        return redirect('member:cancellation')


    r_payment = requests.post('https://api.sandbox.paypal.com/v1/payments/payment',
                              headers={'Content-Type':'application/json',
                                       'Authorization':'Bearer '+r_token.json()['access_token']},
                              data='{\
                                      "intent": "sale",\
                                      "redirect_urls": {\
                                        "return_url": "'+return_url+'",\
                                        "cancel_url": "'+cancel_url+'"\
                                      },\
                                      "payer": {\
                                        "payment_method": "paypal"\
                                      },\
                                      "transactions": [{\
                                        "amount": {\
                                          "total": "1",\
                                          "currency": "EUR"\
                                        }\
                                      }]\
                                    }')

    if r_payment.status_code !=  201 :
        add_message(request, INFO, "Erreur lors de l'initialisation du paiment paypal.\nContactez nous à l'adresse suivante : XXXX.")
        add_message(request, INFO, r_payment.json())
        return redirect('member:cancellation')

    links = {}

    for link in r_payment.json()['links']:
        links[link['rel']] = link['href']

    return HttpResponseRedirect(links['approval_url'])

def subscribeView(request):
    if request.method == "POST":
        form = forms.SubscribeForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]

            existing_users = User.objects.filter(Q(email__iexact=email))

            if not existing_users:
                user = User.objects.create_user(email, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.is_active = False
                user.save()

                return redirect(userPayment, user=user)

            else:
                add_message(request, ERROR, "Erreur lors du traitement du formulaire : cet email est déjà enregistré.")
                form = forms.SubscribeForm()

        else:
            add_message(request, INFO, "Erreur lors du traitement du formulaire.")
            form = forms.SubscribeForm()

    else:
        form = forms.SubscribeForm()

    return render(request, 'subscribe.html', { 'form' : form })
