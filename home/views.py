from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Académie de Danse 4 Temps"
    description = ""
    return render(request, 'home.html', {'title':title, 'description':description})

def about(request):
    title = "À propos"
    description = ""
    return render(request, 'about.html', {'title':title, 'description':description})

def projects(request):
    title = "Nos projets"
    description = ""
    return render(request, 'projects.html', {'title':title, 'description':description})

def news(request):
    title = "Avancées majeures de l'AD4T"
    description = ""
    return render(request, 'news.html', {'title':title, 'description':description})

def communication(request):
    title = "Clubs et communautés de Danse 4 Temps"
    description = ""
    return render(request, 'communication.html', {'title':title, 'description':description})

def ethique(request):
    title = "Travaux du pôle Éthique"
    description = ""
    return render(request, 'ethique.html', {'title':title, 'description':description})

def structuration(request):
    title = "Travaux du pôle Structuration"
    description = ""
    return render(request, 'structuration.html', {'title':title, 'description':description})
