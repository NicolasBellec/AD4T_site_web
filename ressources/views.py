from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from ressources.models import Ressource

# Create your views here.
@login_required()
def ressourcesView(request, page = 0, *opts, **named_opts):
    articles_per_page = 10
    all_articles = Ressource.objects.all()

    # all_articles = Ressource.objects.filter(date__lt=timezone.now())
    #.order_by('-date')[page*articles_per_page, (page+1)*articles_per_page]
    return render(request, 'ressources.html', { 'articles':all_articles })
