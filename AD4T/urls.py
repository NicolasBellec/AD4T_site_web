"""AD4T URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from member.views import validation, cancellation
from media.views import mediaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('passes/', include('passes.urls')),
    path('ressources/', include('ressources.urls')),
    path('contact/', include('contact.urls')),
    path('login/', include('login.urls')),
    path('home/', include('home.urls')),
    path('member/', include('member.urls')),
    path('member:validation', validation),
    path('member:cancellation', cancellation),
    path('media/<str:slug>', mediaView, name='media_url'),
]
