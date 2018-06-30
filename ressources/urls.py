from django.urls import path
from . import views

urlpatterns = [
    path('', views.ressourcesView),
    path('page=<int:page>', views.ressourcesView),
]
