from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts_view')
]
