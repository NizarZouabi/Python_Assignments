from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
from flask_app.models.ninja import Ninja
class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas_list=[] # List to store associated ninjas

    @classmethod
     # Create a new dojo in the database
    def create_dojo(cls,data):
        
        query=" INSERT INTO dojos (name)VALUES (%(name)s);"
        results=MySQLConnection(DATABASE).query_db(query,data)
        return results
 # Retrieve all dojos from the database
    @classmethod
    def show_dojo(cls):
       
        query="SELECT * FROM dojos;"
        results_dojo=MySQLConnection(DATABASE).query_db(query)
        table_dojo=[]
        for row in results_dojo :
            table_dojo.append(cls(row))
        return table_dojo
     # Retrieve ninjas associated with a specific dojo from the database
    @classmethod
    def show_ninja_in_dojo(cls,data):
        query="SELECT * FROM dojos JOIN ninjas on dojos.id=ninjas.dojo_id WHERE dojos.id=%(id)s "
        results=MySQLConnection(DATABASE).query_db(query,data)
        ninjas=[]
        if results:
             # Create a new Dojo object using the first row of results
            this_dojo=cls(results[0])
            # Iterate over each row in the results
            for row in results :
              # Create a dictionary containing the ninja data
             data_test={
                   'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                     'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at']
             }
               # Create a new Ninja object using the data dictionary and append it to the ninjas list
             ninjas.append(Ninja(data_test))
              # Assign the ninjas list to the ninjas_list attribute of the current dojo object
             this_dojo.ninjas_list=ninjas
             # Return the list of ninjas
             return ninjas
            # If no results found, return an empty list
        return []
