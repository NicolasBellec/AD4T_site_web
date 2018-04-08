from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def ressourcesView(request, *opts, **named_opts):
    return render(request, 'ressources.html')
