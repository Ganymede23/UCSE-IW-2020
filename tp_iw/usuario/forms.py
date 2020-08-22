from django import forms

class CargarDatos(forms.Form):

    nombre_apellido = forms.CharField(max_length=100)
    mail = forms.EmailField()
