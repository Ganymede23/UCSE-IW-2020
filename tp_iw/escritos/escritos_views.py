from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, CreateView
from django.utils import timezone

from .models import Escrito
from .forms import EscritoForm
from usuario.models import Profile

def escrito_detail(request, pk):
    escrito = get_object_or_404(Escrito, pk=pk)

    user_logged = request.user

    return render(request, 'escritos_details.html', {'escrito': escrito, 'user_logged': user_logged })

def escrito_new(request):
    if request.method == "POST":
        form = EscritoForm(request.POST)
        if form.is_valid():
            escrito = form.save(commit=False)
            escrito.author = request.user
            escrito.save()
            return redirect('escrito_detail', pk=escrito.pk)
    else:
        form = EscritoForm()

    return render(request, 'add_escrito.html', {'form': form})

def escritos_draft_list(request):
    escritos = Escrito.objects.filter(date__isnull=True).order_by('created_date')
    return render(request, 'escritos_draft_list.html', {'escritos': escritos})

def escrito_publish(request, pk):
    escrito = get_object_or_404(Escrito, pk=pk)
    escrito.publish()
    
    return redirect('escrito_detail', pk=pk)

def publish(self):
    self.date = timezone.now()
    self.save()

def escrito_remove(request, pk):
    escrito = get_object_or_404(Escrito, pk=pk)
    escrito.delete()
    return redirect('/home/homepage')

def escrito_edit(request, pk):
    escrito = get_object_or_404(Escrito, pk=pk)
    if request.method == "POST":
        form = EscritoForm(request.POST, instance=escrito)
        if form.is_valid():
            escrito = form.save(commit=False)
            escrito.author = request.user
            escrito.date = None
            escrito.save()
            return redirect('escrito_detail', pk=escrito.pk)
    else:
        form = EscritoForm(instance=escrito)
    return render(request, 'add_escrito.html', {'form': form})