from django.db.models.aggregates import Avg
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Libro, Review, Rate
from .forms import ReviewForm, RateForm

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

    rates= Rate.objects.filter( review = review)
    rates_usarios = []
    for rate in rates:
        if Rate.objects.filter( usuario=user_logged).exists():
            rates_usarios.append(rate.usuario)

    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.review = review
            rate.usuario = user_logged
            rate.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = RateForm()    

    avg = Rate.objects.values('review').order_by('review').annotate(average_stars=Avg('rating')).filter(review=review)

    return render(request, 'review_detail.html', {'review': review, 'user_logged': user_logged, 'form':form,
     'rates_usuarios':rates_usarios, 'avg':avg })

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

def rate_review (request,pk):
    pass