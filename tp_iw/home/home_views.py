from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from itertools import chain

from escritos.models import Escrito
from libros.models import Review
from usuario.models import Profile

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/home/homepage")
    else:
        return render(request, "index.html")

def placeholder(request):
    return render(request,"placeholder.html")

@login_required(
    login_url="/usuario/login"
)  # el decorador te envia al login si intentas entrar sin loguearte a home

def home_page(request):
    #Obtiene el perfil del user logueado
    profile = Profile.objects.get(user=request.user)

    #Obtiene el 'grupo' al que pertenece el usuario
    if profile.user.groups.filter(name = 'Admins').exists():
        grupo = 'Admin'
    else:
        grupo = 'User'

    #Verifica a quién sigue el usuario logueado
    users = [user for user in profile.following.all()]
    escritos= []
    escritos_seguidos=[]
    escritos_propios=[]
    escritos_leidos=[]

    #Obtener escritos leidos del usuario
    escritos_l = Escrito.objects.all()
    for escrito in escritos_l:
        if profile.escritos_leidos.filter(id=escrito.pk).exists():
            escritos_leidos.append(escrito)

    #Obtener posts de cuentas seguidas
    for usuario in users:
        escritos_seguidos.extend(Escrito.objects.filter(author=usuario).exclude(date = None))

    escritos_propios.extend(list(Escrito.objects.filter(author=profile.user).exclude(date = None)))

    escritos = sorted(chain(escritos_seguidos,escritos_propios),key=lambda instance: instance.date, reverse=True)

    return render(request, 'home_page.html', {'perfil': profile, 'escritos': escritos, 'grupo': grupo, 'eleidos': escritos_leidos, 'epropios': escritos_propios})

'''
def home_page(request):
    #Obtiene el perfil del user logueado
    profile = Profile.objects.get(user=request.user)

    #Obtiene el 'grupo' al que pertenece el usuario
    if profile.user.groups.filter(name = 'Admins').exists():
        grupo = 'Admin'
    else:
        grupo = 'User'
    
    #Verifica a quién sigue el usuario logueado
    users = [user for user in profile.following.all()]
    posts_leidos = []
    posts_no_leidos = []
    escritos_propios = []
    escritos_seguidos = []
    reviews_propios=[]
    reviews_seguidos=[]
    queryset = None

    #Obtener posts de cuentas seguidas
    for usuarios in users:
        escritos_seguidos = Escrito.objects.filter(author=usuarios).exclude(date = None).order_by("date")
        for escrito in escritos_seguidos:
            if  profile.escritos_leidos.filter(id=escrito.pk).exists():
                posts_leidos.append(escrito)
            else:
                posts_no_leidos.append(escrito)
        reviews_seguidos = Review.objects.filter(author=usuarios).exclude(date = None).order_by("created_date")
        #posts_no_leidos.extend(list(reviews_seguidos))

    #Obtener posts propios
    escritos_propios = Escrito.objects.filter(author=profile.user).exclude(date = None).order_by("date")
    for escrito in escritos_propios:
            if profile.escritos_leidos.filter(id=escrito.pk).exists():
                posts_leidos.append(escrito)
            else:
                posts_no_leidos.append(escrito)
    reviews_propios = Review.objects.filter(author=profile.user).exclude(date = None).order_by("created_date")
    #posts_no_leidos.extend(list(reviews_propios))

    escritos = Escrito.objects.all()
        
    return render(request, 'home_page.html', {'perfil': profile, 'posts_leidos': posts_leidos, 'posts_no_leidos': posts_no_leidos, 'grupo': grupo})
'''