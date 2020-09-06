from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.escritos.models import Escrito


def index(request):
    return render(request, "index.html")


@login_required(
    login_url="/usuario/login"
)  # el decorador te envia al login si intentas entrar sin logearte a home
def home_page(request):

    list_escritos = Escrito.objects.all().order_by(
        "date"
    )  # de aca muestra los escritos esta forma de hacerlo lo sque de un ejemplo de fisa basicamente

    return render(request, "home_page.html", {"list_escritos": list_escritos})
