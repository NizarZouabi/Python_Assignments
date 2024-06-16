from django.urls import path
from . import views

urlpatterns = [
    path("", views.books, name='books'),
    path("books/<int:id>/", views.book, name='book'),
    path("authors/", views.authors, name='authors'),
    path("authors/<int:id>/", views.author, name='author'),
    path("add/book/", views.add_book, name='add_book'),
    path("add/author/", views.add_author, name='add_author'),
    path("add/author/book/", views.add_author_book, name='add_author_book'),
    path("add/book/author/", views.add_book_author, name='add_book_author')
]
