from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView

from django.views import generic

# from django.views.generic import ListView, DetailView

import requests
import json

from .forms import CreateUserForm, ChangeUserForm, PasswordChangingForm
from .models import Profile

# =====CREACION Y AUTENTICACION DE USUARIOS======


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]  # recibe campo usuario
        password = request.POST["password"]  # recibe campo password
        user = authenticate(
            request, username=username, password=password
        )  # verifica usuario logeado

        # Remember Me
        if not request.POST.get("remember_me", None):
            request.session.set_expiry(0)

        if user is not None:
            login(request, user)

            return HttpResponseRedirect(
                "/home/homepage"
            )  # si se logea correctamente redirige a home
        else:
            messages.error(request, "Datos inválidos.")

    return render(request, "login.html")


def register(request):

    form = CreateUserForm  # usa el formulario creado en Forms.py

    if (
        request.method == "POST"
    ):  # si le llegan datos los toma y verifica que sean validos

        # reCaptcha de google
        captcha_token = request.POST.get("g-recaptcha-response")
        captcha_url = "https://www.google.com/recaptcha/api/siteverify"
        captcha_secret = "6Ldx7ccZAAAAAE1lFcNx88aMHkB7fCEFK19gWpc_"
        captcha_data = {"secret": captcha_secret, "response": captcha_token}
        captcha_server_response = requests.post(url=captcha_url, data=captcha_data)
        print(request.POST.get("g-recaptcha-response"))
        print(captcha_server_response.text)
        captcha_json = json.loads(captcha_server_response.text)
        if captcha_json["success"] == False:
            messages.error(request, "Captcha inválido.")
            return HttpResponseRedirect("/usuario/register/")

        form = CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False  # lo pone como falso para que necesite la confirmacion por mail para logear
            user.save()

            profile = Profile.objects.create(user=user)

            token = default_token_generator.make_token(
                user
            )  # token para link de verificacion

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))  # crea el id encodeado

            domain = get_current_site(request).domain
            link = reverse(
                "activate", kwargs={"uidb64": uidb64, "token": token}
            )  # arma el link de activacion
            activate_url = "http://" + domain + link

            mail_subject = "Activa tu cuenta"

            mail_body = ( #hay que cambiarlo por una plantilla (render to string)
                "Hola "
                + user.username
                + "!"
                + " Verifica tu cuenta con el siguiente link:\n"
                + activate_url
            )

            to_email = form.cleaned_data.get("email")  # toma el email del usuario

            email = EmailMessage(  # arma el email
                mail_subject, mail_body, to=[to_email]
            )
            email.send(fail_silently=False)

            # redirije a la confirmación de email de verificación
            return HttpResponseRedirect("/usuario/email_confirmation_sent")
        else:
            form = CreateUserForm(request.POST)

    context = {"form": form}

    return render(request, "register.html", context)


def logout_user(request):  # vista para cerrar sesion
    logout(request)
    return HttpResponseRedirect("/home/index/")


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))  # decodea uid
        user = User.objects.get(pk=uid)  # busca usuario

        if not default_token_generator.check_token(user, token):
            messages.error(
                request, "su cuenta ya esta activada"
            )  # por si ya se habia activado

        if user.is_active:
            return render(request, "email_activation.html")
        user.is_active = True  # lo cambia activo para que se pueda logear
        user.save()

        # messages.success(request,'La cuenta se activo correctamente') # es es mensaje que tenemos que hacer aparecer
        return render(request, "email_activation.html")
    except (
        TypeError,
        ValueError,
        OverflowError,
        User.DoesNotExist,
    ):  # si el usuario no existe
        user = None

    return render(request, "email_activation.html")


def email_confirmation_sent(request):
    return render(request, "email_confirmation_sent.html")


# ====PERFIL DE USUARIO=====


class UserEditView(generic.UpdateView):  # editar usuario
    form_class = ChangeUserForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy("/home/home_page")

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    succes_url = reverse_lazy("password_success")


def password_success(self, request):
    return render(request, "password_success.html", {})


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = "user_profile.html"

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])

        context["page_user"] = page_user

        return context
