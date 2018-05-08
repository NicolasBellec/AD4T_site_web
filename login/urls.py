from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('connect', views.connectView),
    path('subscribe', views.subscribeView),
    path('disconnect', views.disconnectView),
]
