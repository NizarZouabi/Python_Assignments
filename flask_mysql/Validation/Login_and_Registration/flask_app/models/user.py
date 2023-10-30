from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.logged_in = data['logged_in']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('fake_fb').query_db(query)

        users = []
        for user in results:
            users.append(cls(user))
        print(users)
        return users
    
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('fake_fb').query_db(query, data)
        
        if not result:
            return None
        print(result)
        return cls(result[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (username, email, password) VALUES (%(username)s, %(email)s, %(password)s);"
        return connectToMySQL('fake_fb').query_db(query, data)
    
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET username = %(username)s, email = %(email)s, password = %(password)s WHERE id = %(id)s;"
        return connectToMySQL('fake_fb').query_db(query, data)
    
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("fake_fb").query_db(query, data)
        
        if len(result) < 1:
            return False
        print(result)
        return cls(result[0])
        
        
    @classmethod
    def get_by_name(cls, data):
        query = "SELECT * FROM users WHERE username = %(username)s;"
        result = connectToMySQL("fake_fb").query_db(query, data)

        if len(result) < 1:
            return False
        print(result)
        return cls(result[0])
    
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        
        if len(user['username']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        if not email_pattern.match(user['email']):
            flash("Not a valid Email.")
            is_valid = False
        
        user_in_database = User.get_by_email(data=user)
        if user_in_database:
            flash('There is an Account with the given Email')
            is_valid = False
        
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        
        if user['password'] != user['password_confirmation']:
            flash("Password Confirmation doesn't match the Password.")
            is_valid = False
        
        return is_valid
