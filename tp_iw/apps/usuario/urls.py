from django.contrib import admin
from django.urls import path, include, re_path

from.usuario_views import login_user,  register, logout_user, activate

urlpatterns = [
    path ('login/', login_user ),
    path('register/', register),
    path('logout_user/', logout_user),
    path('email_activation/', activate),
    path('activate/<uidb64>/<token>/', activate, name='activate'),#path de la activacion del email
]
