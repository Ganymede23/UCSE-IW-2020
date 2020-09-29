from django import forms
from ckeditor.fields import RichTextField
from .models import Review, Rate, Comment_r

class ReviewForm(forms.ModelForm):
    title = forms.CharField (label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': "Titulo"}))

    def __init__(self,*args,**kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        #self.fields['title'].label = "Titulo"
        self.fields['body'].label = ""
        
    class Meta:
        model = Review
        fields = ('title', 'body')

class RateForm(forms.ModelForm):
    estrellas = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5")
    )
    rating = forms.ChoiceField( widget=forms.RadioSelect(attrs={'class': 'rating'}), choices=estrellas, required = True)
    class Meta:
        model = Rate
        fields = ['rating']

class CommentForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ""

    class Meta:
        model = Comment_r
        fields = ['body']