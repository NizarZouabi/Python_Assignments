from app import app
from flask import render_template, request, redirect, session
from app.models import author,book

@app.route('/authors')
def main():
    
    all_auths = author.Author.get_all_authors()
    return render_template('authors.html', all_authors = all_auths)

@app.route('/add/author', methods=['POST'])
def add_author():
    
    data = {
        'name':request.form['name'],
    }
    
    author.Author.save_author(data)
    return redirect('/authors')


@app.route('/authors/<int:id>')
def show_author(id):
    
    data = {
        'id':id
    }
    
    books = book.Book.get_all_books()
    show_author = author.Author.get_author_with_fav_books(data)
    return render_template('author.html', authors=show_author, all_books = books)


@app.route('/add/author/<int:author_id>', methods=['POST'])
def add_favorite(author_id):
    book_id = request.form.get('book')
    data = {
        'book_id':book_id,
        'author_id':author_id
    }
    
    book.Book.add_fav(data)
    return redirect(f'/authors/{author_id}')
