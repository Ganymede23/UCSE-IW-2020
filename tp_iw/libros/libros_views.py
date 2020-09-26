from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Libro, Review
from .forms import ReviewForm

def show_books(request): #vista de paginas libros
    libros = Libro.objects.all()

    return render(request, 'libros.html', {'libros': libros})

def book_detail(request, pk): #detalle de libros
    reviews=[]
    book = get_object_or_404(Libro, pk=pk)
    reviews = Review.objects.filter(book=book, date__isnull=False).order_by('date')

    return render(request, 'libros_detail.html', {'libro':book, 'reviews':reviews})

def review_new(request,pk_libro): # Crear nuevo review
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            book = get_object_or_404(Libro, pk=pk_libro)
            review.book = book
            review.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form})


def review_detail(request, pk): # Detelle de reviews
    review = get_object_or_404(Review, pk=pk)
    user_logged = request.user

    return render(request, 'review_detail.html', {'review': review, 'user_logged': user_logged })

def review_publish(request, pk): # Publicar review
    review = get_object_or_404(Review, pk=pk)
    review.publish()
    
    return redirect('review_detail', pk=pk)

def publish(self): # funcion publicar
    self.date = timezone.now()
    self.save()

def review_remove(request, pk): # borrar review
    review = get_object_or_404(Review, pk=pk)
    review.delete()

    return redirect('/libros/show_books')

def review_edit(request, pk): # funcion para editar review
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.date = None
            review.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)
        
    return render(request, 'add_review.html', {'form': form})