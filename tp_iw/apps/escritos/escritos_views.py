from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, CreateView

from .models import Escrito


class Escrito_Detail_View(DetailView):
    model = Escrito
    template_name = 'escritos_details.html'  

class add_escrito_view (CreateView):
    model = Escrito
    template_name = 'add_escrito.html' 
    #fields = '__all__'
    fields = ('title','body', 'author') 