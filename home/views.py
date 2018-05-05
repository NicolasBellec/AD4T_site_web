from django.shortcuts import render

# Create your views here.
def home(request):
    title = "Académie de Danse 4 Temps"
    description = ""
    home_active = "active"
    return render(request, 'home.html', {'title':title, 'description':description, 'home_active':home_active})
