from django import forms
from ckeditor.fields import RichTextField
from .models import Escrito, Comment

class EscritoForm(forms.ModelForm):

    class Meta:
        model = Escrito
        fields = ('title', 'body')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']