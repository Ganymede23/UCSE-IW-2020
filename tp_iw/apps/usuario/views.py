from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm
import requests
import json

# Create your views here.


def index(request):
    return render(request, "index.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]  # recibe campo usuario
        password = request.POST["password"]  # recibe campo password
        user = authenticate(
            request, username=username, password=password
        )  # verifica usuario logeado

        #Remember Me
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)

        #reCaptcha
        captcha_token=request.POST.get("g-recaptcha-response")
        captcha_url="https://www.google.com/recaptcha/api/siteverify"
        captcha_secret="6LdwXMMZAAAAAH61OADU2Pc-0vge2znwGBsn7l8l"
        captcha_data={"secret":captcha_secret,"response":captcha_token}
        captcha_server_response=requests.post(url=captcha_url,data=captcha_data)
        #print(captcha_server_response)
        #print(captcha_server_response.text)
        captcha_json=json.loads(captcha_server_response.text)
        if captcha_json['success']==False:
            messages.error(request, 'Captcha inválido.')
            return HttpResponseRedirect("/login")

        if user is not None:
            login(request, user)

            return HttpResponseRedirect(
                "/home"
            )  # si se logea correctamente redirige a home
        else:
            messages.error(request, 'Datos inválidos.')

    return render(request, "login.html")


def register(request):

    form = CreateUserForm  # usa el formulario creado en Forms.py

    if (
        request.method == "POST"
    ):  # si le llegan datos los toma y verifica que sean validos
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
        #agregar error de ingreso
    context = {"form": form}

    return render(request, "register.html", context)


@login_required(
    login_url="/login/"
)  # el decorador te envia al login si intentas entrar sin logearte a home
def home(request):
    return render(request, "home.html")


def logout_user(request):  # vista para cerrar sesion
    logout(request)
    return HttpResponseRedirect("/index")