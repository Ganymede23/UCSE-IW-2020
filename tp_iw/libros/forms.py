from django import forms
from .models import Review, Rate, Comment_r, Denuncia_r

class ReviewForm(forms.ModelForm):
    title = forms.CharField (label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': "Titulo"}))

    def __init__(self,*args,**kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields['body'].label = ""
        
    class Meta:
        model = Review
        fields = ('title', 'body')

class RateForm(forms.ModelForm): #formulario para raitear reviews

    estrellas = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5")
    )

    rating = forms.ChoiceField(  #usa la clase rating para poder usar  el css de las estrellas como form
        widget=forms.RadioSelect(attrs={'class': 'rating'}),
        choices=estrellas,
        required = True) 

    class Meta:
        model = Rate
        fields = ['rating']

class CommentForm(forms.ModelForm): #  form de comentarios

    def __init__(self,*args,**kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ""

    class Meta:
        model = Comment_r
        fields = ['body']

class DenunciaForm_r(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(DenunciaForm_r, self).__init__(*args, **kwargs)

        self.fields['descripcion'].label = ""

    class Meta:
        model = Denuncia_r
        fields = ['motivo', 'descripcion']
