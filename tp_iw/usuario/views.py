from django.http import HttpResponseRedirect
from django.shortcuts import render
from usuario.forms import CargarDatos

# Create your views here.

def home(request):
    return  render(request, "home.html")  

def login(request):

    if request.method == 'POST':
        datos_usuario = CargarDatos(request.POST)
    else:
        datos_usuario = CargarDatos()

    return  render(request, "login.html", {'datos_usuario': datos_usuario})



