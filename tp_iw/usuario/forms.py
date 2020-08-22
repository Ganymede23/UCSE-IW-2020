from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#from .models import Order

class CargarDatos(forms.Form):

    #nombre_apellido = forms.CharField(max_length=100)
    #mail = forms.EmailField()

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

#class OrderForm(ModelForm):
#    class Meta:
#        model = Order
#        fields = '__all__' 
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


