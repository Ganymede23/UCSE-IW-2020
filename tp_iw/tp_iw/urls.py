"""tp_iw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic.base import TemplateView

#para cargar  imagenes y statics
from django.conf import settings
from django.conf.urls.static import static

from home.home_views import index 

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #home
    path('', index, name='index'),
    path('home/', include('home.urls')),

    #usuario
    path('usuario/', include('usuario.urls')),

    #libros
    path('libros/', include('libros.urls')),

    #allauth
    path('accounts/', include('allauth.urls')),

    #Escritos
    path('escritos/', include('escritos.urls')),

    #Robots
    path('robots.txt/', include('robots.urls')),

    #Search
    path('search/', include('haystack.urls')),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
