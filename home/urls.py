from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_view'),
    path('about', views.about, name='about_view'),
    path('projects', views.projects, name='projects_view'),
    path('news', views.news, name='news_view')
]
