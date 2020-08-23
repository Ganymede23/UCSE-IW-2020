from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CargarDatos, CreateUserForm
from django.contrib.auth.decorators import login_required

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
            #return redirect('home_logueado')
            return HttpResponseRedirect('/home_logueado')
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

@login_required(login_url='/login/')
def home_logueado(request):
    return  render(request, "home_logueado.html") 

def prueba(request):
    return  render(request, "prueba.html")

def logout_user(request):
    logout(request) 
    return HttpResponseRedirect('/home')




