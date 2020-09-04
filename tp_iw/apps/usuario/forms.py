from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):  # creacion de formulario de registracion a partir de UserCreationForm

    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Correo electrónico"}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self,*args,**kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = "Nombre de usuario"

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = "Contraseña"

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = "Confirmar contraseña"

