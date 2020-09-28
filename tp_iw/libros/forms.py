from django import forms
from ckeditor.fields import RichTextField
from .models import Review, Rate




class ReviewForm(forms.ModelForm):

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
    rating = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'rating'}), choices=estrellas)
    class Meta:
        model = Rate
        fields = ['rating']