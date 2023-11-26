from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
class Ninja:
     def __init__(self,data):
        self.id=data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age=data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # create ninjas
     @classmethod
     def create_ninja(cls,data):
          # Define the MySQL query to retrieve all ninjas from the database
         query="INSERT INTO ninjas(first_name,last_name,age,dojo_id)VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
          # Execute the query using the MySQLConnection and retrieve the results
         return MySQLConnection(DATABASE).query_db(query,data)
    # read ninjas
     @classmethod
     def get_all_ninja(cls):
          # Define the MySQL query to retrieve all ninjas from the database
         query="SELECT * FROM ninjas; "
          # Execute the query using the MySQLConnection and retrieve the results
         results=MySQLConnection(DATABASE).query_db(query)
# Create an empty list to store the Ninja objects
         table_ninjas=[]
          # Iterate over each row in the results
         for row in results :
             # Create a new Ninja object using the current row data and add it to the list
             table_ninjas.append(cls(row))
              # Return the list of Ninja objects
         return table_ninjas