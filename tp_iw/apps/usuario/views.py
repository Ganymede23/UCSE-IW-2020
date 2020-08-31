from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.urls import reverse

import requests
import json


from .forms import CreateUserForm
#from .tokens import account_activation_token

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

            user = form.save(commit=False)
            user.is_active = False # lo pone como falso para que necesite la confirmacion por mail para logear
            user.save()

            token = default_token_generator.make_token(user)# token para link de verificacion

            uidb64= urlsafe_base64_encode(force_bytes(user.pk)) # crea el id encodeado

            domain = get_current_site(request).domain
            link= reverse('activate', kwargs={'uidb64':uidb64,'token':token}) # arma el link de activacion
            activate_url = domain+link # le agrega el dominio al link

            mail_subject = 'Activa tu cuenta' 

            mail_body = 'Hola '+ user.username + '!' + \
                ' Verifica tu cuenta con el siguiente link:\n' + activate_url

            to_email = form.cleaned_data.get('email') # toma el email del usuario
            
            email = EmailMessage( # arma el email
                        mail_subject, 
                        mail_body, 
                        to=[to_email]
            )
            email.send(fail_silently=False)

            # redirije al login
            return HttpResponseRedirect("/login")
        else:
            form = CreateUserForm(request.POST)

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


 # esta es otra forma pero deje la otra porque creo que es mas linda,igual no se
'''def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse("su cuenta se activo")
    else:
        return HttpResponse("/login")'''

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64)) #decodea uid
        user = User.objects.get(pk=uid)#busca usuario

        if not default_token_generator.check_token(user,token):
            return HttpResponseRedirect('/login'+'?message='+'El usuario ya esta activado') # por si ya se habia activado

        if user.is_active:
            return render(request, 'login.html')
        user.is_active=True #lo cambia activo para que se pueda logear
        user.save()   

        # messages.success(request,'La cuenta se activo correctamente') # es es mensaje que tenemos que hacer aparecer
        return render(request, 'login.html')
    except(TypeError, ValueError, OverflowError, User.DoesNotExist): #si el usuario noo existe
        user = None

   
    return render(request, 'login.html') #