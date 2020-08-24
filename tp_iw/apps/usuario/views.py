from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

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
        if user is not None:
            login(request, user)

            return HttpResponseRedirect(
                "/home"
            )  # si se logea correctamente redirige a home_logeado / home

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
)  # el decorador te envia al login si intentas entrar sin logearte a home_logueado
def home(request):
    return render(request, "home.html")


def logout_user(request):  # vista para cerrar sesion
    logout(request)
    return HttpResponseRedirect("/index")
