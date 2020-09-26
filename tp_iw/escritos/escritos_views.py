from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Escrito, Comment
from .forms import EscritoForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def escrito_detail(request, pk): # Detelle de escritos
    escrito = get_object_or_404(Escrito, pk=pk)

    user_logged = request.user

    total_likes = escrito.total_likes()

    liked = False
    if escrito.likes.filter(id=request.user.id).exists():
        liked = True

    comments = Comment.objects.filter(escrito = escrito)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.escrito = escrito
            comment.usuario = request.user
            comment.save()
            return redirect('escrito_detail', pk=escrito.pk)
    else:
        form = CommentForm()
        #form.body = ""

    return render(request, 'escritos_details.html', {'escrito': escrito, 'user_logged': user_logged, 'total_likes': total_likes, 'liked': liked, 'comments': comments, 'form': form })

def escrito_new(request): # Crear nuevo escrito
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

def escrito_publish(request, pk): # Publicar escrito
    escrito = get_object_or_404(Escrito, pk=pk)
    escrito.publish()
    
    return redirect('escrito_detail', pk=pk)

def publish(self): # funcion publicar
    self.date = timezone.now()
    self.save()

def escrito_remove(request, pk): # borrar escrito
    escrito = get_object_or_404(Escrito, pk=pk)
    escrito.delete()
    return redirect('/home/homepage')

def escrito_edit(request, pk): # funcion para editar escrito
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

def like_escrito(request, pk):
    escrito = get_object_or_404(Escrito, id=request.POST.get('post_id'))
    liked = False
    if escrito.likes.filter(id=request.user.id).exists():
        escrito.likes.remove(request.user)
        liked = False
    else:
        escrito.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('escrito_detail', args=[str(pk)]))

# def comment_escrito(request, pk):
#     escrito = get_object_or_404(Escrito, id=request.POST.get('post_id'))
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.usuario = request.user
#             comment.save()
#             #return redirect('escrito_detail', pk=escrito.pk)

#     return HttpResponseRedirect(reverse('escrito_detail', args=[str(pk)]))

def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    pk = comment.escrito.pk
    comment.delete()

    return redirect('escrito_detail', pk=pk)