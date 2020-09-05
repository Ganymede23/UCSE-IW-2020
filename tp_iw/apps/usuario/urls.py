from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from.usuario_views import login_user,  register, logout_user, activate, UserEditView,PasswordsChangeView,password_success, ShowProfilePageView

urlpatterns = [
    path ('login/', login_user ),
    path('register/', register),
    path('logout_user/', logout_user),
    path('email_activation/', activate),
    path('activate/<uidb64>/<token>/', activate, name='activate'),#path de la activacion del email
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_done.html"), name="password_reset_complete"),
    path('password/',PasswordsChangeView.as_view(template_name="change_password.html")),
    path('password_success/', password_success, name='password_success' ),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page')
]
