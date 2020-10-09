from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Escrito, Comment, Denuncia
from .forms import EscritoForm, CommentForm, DenunciaForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from usuario.models import Profile


def escrito_detail(request, pk): # Detelle de escritos
    escrito = get_object_or_404(Escrito, pk=pk)
    body = escrito.body.split(' ')
    tiempo = ((len(body)*60)/320)*1000
    user_logged = request.user

    total_likes = escrito.total_likes()

    liked = False
    if escrito.likes.filter(id=request.user.id).exists():
        liked = True

    comments = Comment.objects.filter(escrito = escrito)

    #comments_denunciados = []
    #for comment in comments:
    #    if comment.denuncias.filter(id=request.user.id).exists():
    #        comments_denunciados.append(comment)

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

    return render(request, 'escritos_details.html', {'escrito': escrito, 'user_logged': user_logged, 'total_likes': total_likes, 'liked': liked, 'comments': comments, 'form': form, 'tiempo': tiempo })

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

def like_escrito(request, pk): #funcion like
    escrito = get_object_or_404(Escrito, id=request.POST.get('post_id'))
    liked = False
    if escrito.likes.filter(id=request.user.id).exists():
        escrito.likes.remove(request.user)
        liked = False
    else:
        escrito.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('escrito_detail', args=[str(pk)]))

def delete_comment(request, pk): #borrar comentario
    comment = Comment.objects.get(pk=pk)
    pk = comment.escrito.pk
    comment.delete()

    return redirect('escrito_detail', pk=pk)

def denuncia_comment(request, pk): #denunciar comentario
    comment = Comment.objects.get(pk=pk)
    pk = comment.escrito.pk
    #denunciado = False
    #if not comment.denuncias.filter(id=request.user.id).exists():
    #    comment.denuncias.add(request.user)
    #    if comment.total_denuncias() >= 10:
    #       comment.delete()
    denuncias = Denuncia.objects.all()
    
    if request.method == "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.usuario = request.user
            denuncia.comment = comment
            if not denuncias.filter(usuario=request.user.id, comment=comment).exists():
                denuncia.save()
            return redirect('escrito_detail', pk=pk)
    else:
        form = DenunciaForm()

    return render(request, 'add_denuncia.html', {'form': form})

def escrito_leido(request): #marca escrito como leido y lo agrega a la lista de leidos
    if request.POST:
        pk = request.POST['pk']
        userid = request.user.id
        escrito = get_object_or_404(Escrito, pk=pk)
        profile = get_object_or_404(Profile, pk=userid)
        if not profile.escritos_leidos.filter(id=userid).exists():
            profile.escritos_leidos.add(escrito)
            mensaje = 'Ok!'
    else:
        mensaje = 'No POST'

    return JsonResponse({
        'mensaje': mensaje,
        'url': reverse('escrito_detail'),
    })