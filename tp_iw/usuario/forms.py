from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from .models import Profile

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


class ChangeUserForm(UserChangeForm):  # creacion de formulario de editar usuarios

    username = forms.CharField (label='Nombre de usuario',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo electrónico',max_length=200, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField (required=False, label='Nombre',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField (required=False, label='Apellido',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password" ]

class PasswordChangingForm(PasswordChangeForm):  # creacion de cambiar contraseña

    old_password = forms.CharField (label='',max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': "Contraseña actual"}))
    new_password1 = forms.CharField(label='',max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': "Nueva contraseña"}))
    new_password2 = forms.CharField (label='',max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': "Confirmar nueva contraseña"}))
    
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2" ]

class EditProfileForm(forms.ModelForm):
    bio = forms.CharField(label='Biografía', widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].label = "Foto de perfil"
        self.fields['bio'].widget.attrs['rows'] = 3
    class Meta:
        model = Profile
        fields = ("bio", "profile_pic")


