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
from django.contrib.auth.decorators import login_required

#from apps.usuario.usuario_views import login_user,  register, logout_user, activate

from apps.home.home_views import index #, home_page
#from apps.home import home_views

#from apps.escritos.escritos_views import escritodetail

urlpatterns = [
    #adminn
    path('admin/', admin.site.urls),

    #home
    path('', index, name='index'),
    path('home/', include('apps.home.urls')),

    #usuario
    path('usuario/', include('apps.usuario.urls')),

    #allauth
    path('accounts/', include('allauth.urls')),

    #Escritos
    path('escritos/', include('apps.escritos.urls'))
]
