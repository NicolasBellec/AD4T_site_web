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
