from datetime import datetime
from django.shortcuts import render
from books.models import Book
from datetime import timedelta


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {"books": books}
    return render(request, template, context)


def books_by_pub_view(request, pub_date):
    template = 'books/books_list.html'
    books_selection = Book.objects.filter(pub_date=pub_date)

    prev_date = Book.objects.filter(pub_date__lt=pub_date).order_by(
        '-pub_date').values_list('pub_date', flat=True).first()
    next_date = Book.objects.filter(pub_date__gt=pub_date).order_by(
        'pub_date').values_list('pub_date', flat=True).first()

    context = {
        "books": books_selection,
        "prev_date": prev_date,
        "next_date": next_date,
    }

    return render(request, template, context)
