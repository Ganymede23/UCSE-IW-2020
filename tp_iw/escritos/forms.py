from django import forms
from ckeditor.fields import RichTextField
from .models import Escrito

class EscritoForm(forms.ModelForm):

    class Meta:
        model = Escrito
        fields = ('title', 'body')