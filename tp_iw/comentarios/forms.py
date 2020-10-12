from django import forms
from .models import Comment, Denuncia

class CommentForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['body'].label = ""

    class Meta:
        model = Comment
        fields = ['body']

class DenunciaForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super(DenunciaForm, self).__init__(*args, **kwargs)

        self.fields['descripcion'].label = ""

    class Meta:
        model = Denuncia
        fields = ['motivo', 'descripcion']