from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewBlog, name='blog_view'),
]
