from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.owner = None
        self.likes = []
        
        
    def is_liked_by(self, user_id):
        for like in self.likes:
            if like.id == user_id:
                return True
        return False
        
    @classmethod
    def get_recipe_with_likes(cls,data):
        query = """
        SELECT * FROM recipes
        LEFT JOIN users
        ON recipes.user_id = users.id
        LEFT JOIN likes
        ON recipes.id = likes.recipe_id
        LEFT JOIN users AS liked_by
        ON likes.user_id = liked_by.id
        WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL('recipes_schema').query_db(query,data)
        if not results:
            return None
        this_recipe = cls(results[0])
        
        recipe_owner_data = {
            'id':results[0]['users.id'],
            'first_name':results[0]['first_name'],
            'last_name':results[0]['last_name'],
            'email':results[0]['email'],
            'password':results[0]['password'],
            'created_at':results[0]['users.created_at'],
            'updated_at':results[0]['users.updated_at']
        }
        
        recipe_owner = user.User(recipe_owner_data)
        this_recipe.owner = recipe_owner
        
        for result in results:
            if not result['likes.user_id'] == None:
                user_liked_data = {
                    'id':result['liked_by.id'],
                    'first_name':result['liked_by.first_name'],
                    'last_name':result['liked_by.last_name'],
                    'email':result['liked_by.email'],
                    'password':result['liked_by.password'],
                    'created_at':result['liked_by.created_at'],
                    'updated_at':result['liked_by.updated_at']
                    }
                this_recipe.likes.append(user.User(user_liked_data))
        
        return this_recipe
    
    @classmethod
    def get_recipes_with_likes(cls):
        query = """
        SELECT * FROM recipes
        LEFT JOIN users
        ON recipes.user_id = users.id
        LEFT JOIN likes
        ON recipes.id = likes.recipe_id
        LEFT JOIN users AS liked_by
        ON likes.user_id = liked_by.id ORDER BY recipes.id
        """
        results = connectToMySQL('recipes_schema').query_db(query)
        if not results:
            return None
        recipes = []
        this_recipe = None
        for result in results:
            if this_recipe == None or this_recipe.id != result['id']:
                this_recipe = cls(result)
                user_data = {
                    'id':result['users.id'],
                    'first_name': result['first_name'],
                    'last_name': result['last_name'],
                    'email': result['email'],
                    'password': result['password'],
                    'created_at': result['users.created_at'],
                    'updated_at': result['users.updated_at']
                }
                this_recipe.owner = user.User(user_data)
                recipes.append(this_recipe)
            if not result['likes.user_id'] == None:
                user_liked_data = {
                    'id': result['liked_by.id'],
                    'first_name': result['liked_by.first_name'],
                    'last_name': result['liked_by.last_name'],
                    'email': result['liked_by.email'],
                    'password': result['liked_by.password'],
                    'created_at': result['liked_by.created_at'],
                    'updated_at': result['liked_by.updated_at']
                              }
                this_recipe.likes.append(user.User(user_liked_data))
                
        return recipes
        
    @classmethod
    def add_like(cls, data):
        query = "INSERT INTO likes (user_id, recipe_id) VALUES (%(user_id)s, %(recipe_id)s)"
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    @classmethod
    def remove_like(cls, data):
        query = "DELETE FROM likes WHERE recipe_id = %(recipe_id)s AND user_id = %(user_id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)

        recipes = []
        for result in results:
            new_recipe = cls(result)
            recipes.append(new_recipe)
        return recipes
    
    @classmethod
    def get_all_users_with_recipes(cls):
        query = """
        SELECT * FROM recipes
        JOIN users
        ON recipes.user_id = users.id
        """
        results = connectToMySQL('recipes_schema').query_db(query)

        all_recipes = []
        if not results:
            return None
        for result in results:
            if result:
                new_recipe = cls(result)
            user_dict = {
                "id": result["users.id"],
                "first_name": result["first_name"],
                "last_name": result["last_name"],
                "email": result["email"],
                "password": result["password"],
                "created_at": result["users.created_at"],
                "updated_at": result["users.updated_at"]
            }

            owner_data = user.User(user_dict)
            new_recipe.owner = owner_data

            all_recipes.append(new_recipe)

        return all_recipes
    

    @classmethod
    def get_all_recipes_by_user_id(cls,data):
        query = "SELECT * FROM recipes WHERE user_id = %(user_id)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        
        if not results:
            return None

        recipes = [cls(result) for result in results]
        return recipes
    
    
    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)

        if not result:
            return None
        print(result)
        return cls(result[0])
    
    
    @classmethod
    def get_recipe_with_owner(cls, data):
        
        
        query="""
        SELECT * FROM recipes
        LEFT JOIN users
        ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL('recipes_schema').query_db(query,data)
        
        if results:
            this_recipe = cls(results[0])
        else:
            return False
        
        owner_data = {
            "id":results[0]["users.id"],
            "first_name":results[0]["first_name"],
            "last_name": results[0]["last_name"],
            "email": results[0]["email"],
            "password": results[0]["password"],
            "created_at": results[0]["users.created_at"],
            "updated_at": results[0]["users.updated_at"]
        }
        
        this_owner = user.User(owner_data)
        this_recipe.owner = this_owner
        
        return this_recipe
        
    
    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO recipes (name, description, instructions, date, under_30_min, user_id) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under_30_min)s, %(user_id)s);
        """
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under_30_min = %(under_30_min)s
        WHERE id = %(id)s;
        """
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
            
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
            
        if len(recipe['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
            
        if not recipe['date']:
            flash("Please add a Date.")
            is_valid = False
        
        if 'under_30_min' not in recipe:
            flash("Please Select Yes or No.")
            is_valid = False
            
        return is_valid
    