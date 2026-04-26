from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    average_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {"books": books, "num_books": num_books, "average_rating": average_rating})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book-detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })

