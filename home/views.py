from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Académie de Danse 4 Temps"
    description = ""
    return render(request, 'home.html', {'title':title, 'description':description})
