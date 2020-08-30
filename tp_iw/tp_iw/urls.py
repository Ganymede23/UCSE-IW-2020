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
from django.urls import path, include, re_path
from apps.usuario.views import login_user, index, register, home, logout_user, activate
from django.contrib.auth.decorators import login_required
from apps.usuario import views

urlpatterns = [
    path('', views.index, name='/index'),
    path('admin/', admin.site.urls),
    path('login/', login_user),
    path('index/', index),
    path('register/', register),
    path('home/', home),
    path('logout_user/', logout_user),
    path('activate/<uidb64>/<token>/', activate, name='activate'),#path de la activacion del email
    #allauth
    path('accounts/', include('allauth.urls')),
]
