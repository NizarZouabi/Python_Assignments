from app import app
from flask import render_template, request, redirect, session
from app.models import book,author


@app.route('/books')
def books():

    all_bks = book.Book.get_all_books()
    return render_template('books.html', all_books=all_bks)


@app.route('/add/book', methods=['POST'])
def add_book():

    data = {
        'title': request.form['title'],
        'num_of_pages':request.form['num_of_pages']
    }

    book.Book.save_book(data)
    return redirect('/books')


@app.route('/books/<int:id>')
def show_book(id):

    data = {
        'id':id
    }

    authors = author.Author.get_all_authors()
    show_book = book.Book.get_one_book_with_favorating_authors(data)
    return render_template('book.html', books=show_book, all_authors=authors)


@app.route('/add/book/<int:book_id>', methods=['POST'])
def add_fav(book_id):
    authorr_id = request.form.get('author')
    data = {
        'author_id': authorr_id,
        'book_id': book_id,
    }

    book.Book.add_fav(data)
    return redirect(f'/books/{book_id}')
