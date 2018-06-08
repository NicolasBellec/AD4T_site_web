from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import add_message, INFO, ERROR
from . import forms

# Create your views here.
def validation(request):
    context = {}

    api_url = 'https://api.sandbox.paypal.com/v1/payments/payment/'
    execute_url = api_url + request.GET.get('paymentId') + "/execute"

    r_token = requests.post('https://api.sandbox.paypal.com/v1/oauth2/token',
                       headers={'Accept':'application/json',
                                'Accept-Language':'FR'},
                       auth=('XXXX','XXXX'),
                       data={'grant_type':'client_credentials'})

    if r_token.status_code !=  200:
        add_message(request, INFO, "Erreur lors de la récupération du token paypal.\nContactez nous à l'adresse suivante : XXXX.")
        return redirect('member:cancellation')

    r_execute = requests.post(execute_url, headers={'Content-Type':'application/json', 'Authorization':'Bearer '+r_token.json()['access_token']}, data='{"payer_id": "'+request.GET.get('PayerID')+'"}')

    if r_execute.status_code !=  200:
        add_message(request, INFO, "Erreur lors de la validation du paiment paypal.\nContactez nous à l'adresse suivante : XXXX.")
        return redirect('member:cancellation')

    if r_execute.json()['state'] == "approved":
        profil = request.user.profil
        profil.subscribed = True
        profil.save()
        genMemberCard(request.user.username, request.user.first_name, request.user.last_name)
    else:
        context['message'] = "Votre cotisation n'a pas pu aboutir pour la raison suivante : " + r_execute.json()['failure_reason'] + "\nContactez nous à l'adresse suivante : XXXX."

    return render(request, 'validation.html', context)

def cancellation(request):
    context = {}
    
    return render(request, 'cancellation.html', context)
