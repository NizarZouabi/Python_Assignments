from app.config.mysqlconnection import connectToMySQL
from app.models import book

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []
        
        
        
    @classmethod
    def get_author_with_fav_books(cls,data):
        query ="""
        SELECT * FROM authors
        LEFT JOIN favorites
        ON authors.id = favorites.author_id
        LEFT JOIN books AS favorited
        ON favorites.book_id = favorited.id
        WHERE authors.id = %(id)s
        """
        results = connectToMySQL('books_schema').query_db(query, data)
        
        if not results:
            return False
        this_author = cls(results[0])
        
        for result in results:
        
            if result['favorited.id'] is not None:
                books_data = {
                    'id': result['favorited.id'],
                    'title':result['title'],
                    'num_of_pages':result['num_of_pages'],
                    'created_at':result['favorited.created_at'],
                    'updated_at':result['favorited.updated_at']
                }

                this_author.favorites.append(book.Book(books_data))
                
        return this_author
    
    @classmethod
    def save_author(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL('books_schema').query_db(query,data)
    
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL('books_schema').query_db(query)
        all_authors = []
        for result in results:
            if result:
                author_data = {
                    'id':result['id'],
                    'name':result['name'],
                    'created_at':result['created_at'],
                    'updated_at':result['updated_at']
                }
                all_authors.append(cls(author_data))
        return all_authors