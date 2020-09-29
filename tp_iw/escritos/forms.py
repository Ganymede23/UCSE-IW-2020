from django import forms
from ckeditor.fields import RichTextField
from .models import Escrito, Comment

class EscritoForm(forms.ModelForm):
    title = forms.CharField (label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': "Titulo"}))

    def __init__(self,*args,**kwargs):
        super(EscritoForm, self).__init__(*args, **kwargs)

        #self.fields['title'].label = "Titulo"
        self.fields['body'].label = ""

    class Meta:
        model = Escrito
        fields = ('title', 'body')

class CommentForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        #self.fields['title'].label = "Titulo"
        self.fields['body'].label = ""

    class Meta:
        model = Comment
        fields = ['body']