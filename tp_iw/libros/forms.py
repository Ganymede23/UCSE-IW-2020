from django import forms
from ckeditor.fields import RichTextField
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'body')