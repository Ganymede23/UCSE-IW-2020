from django.shortcuts import render,redirect
from .forms import  DenunciaForm
from .models import Comment, Denuncia, MotivoDenuncia
from django.db.models.aggregates import Count

def delete_comment(request, pk): #borrar comentario
    comment = Comment.objects.get(pk=pk)

    if comment.escrito is not None:
        pk_escrito = comment.escrito.pk
        comment.delete()
        return redirect('escrito_detail', pk=pk_escrito)       
    else:
        pk_review = comment.review.pk
        comment.delete()
        return redirect('review_detail', pk=pk_review)  

def denuncia_comment(request, pk): #denuncia un comentario y lo agrega a una lista de denuncias
    
    comment = Comment.objects.get(pk=pk)
    denuncias = Denuncia.objects.all() 

    if request.method == "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.usuario = request.user
            denuncia.comment = comment
            if not denuncias.filter(usuario=request.user.id, comment=comment).exists():
                denuncia.save()

        if comment.escrito is not None:
            pk = comment.escrito.pk  
            return redirect('escrito_detail', pk=pk) 
        else:
            pk = comment.review.pk
            return redirect('review_detail', pk=pk)
    else:
        form = DenunciaForm()

    pk_escrito = comment.escrito.pk

    return render(request, 'add_denuncia.html', {'form': form, 'pk': pk_escrito})

def mostrar_denuncias(request):
    denuncias_comments = Denuncia.objects.all()
    comments =[]
    for denuncia in denuncias_comments:
        comments.append(denuncia.comment)
    comments = set(comments)

    cantidad_denuncias = Denuncia.objects.values('comment').annotate(dcount=Count('comment'))
    cantidad_motivos = Denuncia.objects.values('motivo', 'comment').annotate(dcount=Count('motivo'))

    motivos = MotivoDenuncia.objects.all()


    return render(request, 'mostrar_denuncias.html', {'denuncias_comments': denuncias_comments, 'comments':comments,
     'cantidad_d': cantidad_denuncias, 'cantidad_m':cantidad_motivos, 'motivos': motivos})

def delete_comment_denunciado(request, pk): #borrar comentario
    comment = Comment.objects.get(pk=pk)
    comment.delete()

    return redirect('mostrar_denuncias')

def delete_denuncias(request, pk): #borrar comentario
    comment = Comment.objects.get(pk=pk)
    denuncias_comments = Denuncia.objects.all()
    denuncias_comments= denuncias_comments.filter(comment=comment)
    denuncias_comments.delete()

    return redirect('mostrar_denuncias')

def denuncia_detail(request, pk):
    comment = Comment.objects.get(pk=pk)
    denuncias_comments = Denuncia.objects.all()
    denuncias_comments= denuncias_comments.filter(comment=comment)

    return render(request, 'denuncia_detail.html', {'denuncias_comments': denuncias_comments, 'comment':comment})