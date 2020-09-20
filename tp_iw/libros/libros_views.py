from django.shortcuts import render, redirect, get_object_or_404

from .models import Libro, Review

def show_books(request):

    libros = Libro.objects.all()

    return render(request, 'libros.html', {'libros': libros})

def book_detail(request, pk):

    book = get_object_or_404(Libro, pk=pk)

    return render(request, 'libros_detail.html', {'libro':book})