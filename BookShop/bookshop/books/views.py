from django.shortcuts import render
from .models import Book


def home(request):
    return render(request, 'home.html')

def browse_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'browse_books.html', context)