from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def display(word):
        print(word)
    def __init__(self, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        
        
        #
        # Initialize Connection
           #
        self.client = MongoClient('mongodb://%s:%s/%s.%s' % (HOST,PORT, DB, COL))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            result = self.database.animals.find(data)
            return result
        else:
            raise Exception("Nothing to find, because data parameter is empty")
            
# Create method to implement the U in CRUD.
    def update(self, myQuery, newValues):
        if myQuery is not None:
            x = self.database.animals.update_many(myQuery, newValues)
            return x.modified_count
        else:
            raise Exception("Nothing to update, because myQuery paramter is empty")            

            
# Create method to implement the D in CRUD.
    def delete(self, myQuery):
        if myQuery is not None:
            x = self.database.animals.delete_many(myQuery)
            return x.deleted_count
        else:
            raise Exception("Nothing to delete, becasue myQuery is empty")