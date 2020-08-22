from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CargarDatos, CreateUserForm

# Create your views here.

def home(request):
    return  render(request, "home.html")  

def login_user(request):
    if request.method == 'POST':
        #datos_usuario = CargarDatos(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_logueado')
            #redirect()

    #else:
    #    datos_usuario = CargarDatos()
    #context = {}
    return  render(request, "login.html")

def register(request):

    form = CreateUserForm
    
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}

    return render(request, 'register.html', context)

def home_logueado(request):
    return  render(request, "home_logueado.html") 

def prueba(request):
    return  render(request, "prueba.html") 




