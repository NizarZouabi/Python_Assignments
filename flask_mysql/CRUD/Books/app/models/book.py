from app.config.mysqlconnection import connectToMySQL
from app.models import author

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author = None
        self.favorites = []
        
        
    @classmethod
    def get_one_book_with_favorating_authors(cls,data):
        query ="""
        SELECT * FROM books
        LEFT JOIN favorites
        ON books.id = favorites.book_id
        LEFT JOIN authors AS favorited_by
        ON favorites.author_id = favorited_by.id
        WHERE books.id = %(id)s;
        """
        results = connectToMySQL('books_schema').query_db(query,data)
        
        if not results:
            return False
        this_book = cls(results[0])
        
        for result in results:
                
            if result['favorited_by.id'] is not None:
                authors = {
                'id': result['favorited_by.id'],
                'name':result['name'],
                'created_at': result['favorited_by.created_at'],
                'updated_at': result['favorited_by.updated_at']
                }
                this_book.favorites.append(author.Author(authors))
        
        return this_book
    
    
    @classmethod
    def save_book(cls,data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL('books_schema').query_db(query,data)
        
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL('books_schema').query_db(query)
        all_books = []
        for result in results:
            if result:
                book_data = {
                    'id': result['id'],
                    'title': result['title'],
                    'num_of_pages':result['num_of_pages'],
                    'created_at': result['created_at'],
                    'updated_at': result['updated_at']
                }
                all_books.append(cls(book_data))
        return all_books
    
    @classmethod
    def add_fav(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s)"
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def get_all_with_all(cls):
        pass