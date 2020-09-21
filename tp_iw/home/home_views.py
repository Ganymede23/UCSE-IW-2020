from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from usuario.models import Profile
from itertools import chain

from escritos.models import Escrito
from libros.models import Review

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/home/homepage")
    else:
        return render(request, "index.html")

@login_required(
    login_url="/usuario/login"
)  # el decorador te envia al login si intentas entrar sin loguearte a home

def home_page(request):
    #Obtiene el perfil del user logueado
    profile = Profile.objects.get(user=request.user)
    
    #Verifica a quién sigue el usuario logueado
    users = [user for user in profile.following.all()]
    posts = []
    escritos_propios = []
    escritos_seguidos = []
    reviews_propios=[]
    reviews_seguidos=[]
    queryset = None

    #Obtener posts de cuentas seguidas
    for usuarios in users:
        escritos_seguidos = Escrito.objects.filter(author=usuarios).exclude(date = None)
        posts.append(escritos_seguidos)
        reviews_seguidos = Review.objects.filter(author=usuarios).exclude(date = None)
        posts.append(reviews_seguidos)


    #Obtener posts propios
    escritos_propios = Escrito.objects.filter(author=profile.user).exclude(date = None)
    posts.append(escritos_propios)
    reviews_propios = Review.objects.filter(author=profile.user).exclude(date = None)
    posts.append(reviews_propios)

    if len(posts)>0:
        queryset = sorted(chain(*posts), reverse=True, key=lambda obj: obj.date)
        
    return render(request, 'home_page.html', {'perfil': profile, 'escritos': queryset})
   