from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('', views.connectView),
    path('connect', views.connectView),
    path('disconnect', views.disconnectView),
]
