from haystack import indexes
from ckeditor.fields import RichTextField
from .models import Escrito

class EscritoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    date = indexes.DateTimeField(model_attr='date')

    def get_model(self):
        return Escrito

    def index_queryset(self, using=None):
        '''Queremos que se indexen todas los escritos que tengan date=Nonee'''
        return self.get_model().objects.exclude(date = None)