from django.shortcuts import render, redirect
from .models import Books, Authors

# Create your views here.

def books(request):
    all_books = Books.objects.all()
    context = {"all_books": all_books}
    return render(request, "books.html", context)

def authors(request):
    all_authors = Authors.objects.all()
    context = {"all_authors": all_authors}
    return render(request, "authors.html", context)

def book(request, id):
    this_book = Books.objects.get(id=id)
    all_authors = Authors.objects.exclude(books=this_book)
    context = {
        "book":this_book,
        "authors":all_authors
        }
    return render(request, "bookdetails.html", context)

def author(request, id):
    this_auth = Authors.objects.get(id=id)
    all_books = Books.objects.exclude(authors=this_auth)
    context = {
        "auth":this_auth,
        "books":all_books
        }
    return render(request, "authdetails.html", context)


def add_book(request):
    title = request.POST.get('title')
    desc = request.POST.get('description')
    new_book = Books.objects.create(title=title, desc=desc)
    new_book.save()
    return redirect('/')

def add_author(request):
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    notes = request.POST.get('notes')
    new_author = Authors.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    new_author.save()
    return redirect('/authors')

def add_book_author(request):
    book_id = request.POST.get('book_id')
    book = Books.objects.get(id=book_id)
    author_id = request.POST.get('author_id')
    author = Authors.objects.get(id=author_id)
    book.authors.add(author)
    return redirect('/')

def add_author_book(request):
    author_id = request.POST.get('author_id')
    author = Authors.objects.get(id=author_id)
    book_id = request.POST.get('book_id')
    book = Books.objects.get(id=book_id)
    author.books.add(book)
    return redirect('/authors')
