# Programmer: Mohymin Islam
# This program is desigen to connect mongodb with Python for CRUD operation.

#import pymongo, mongo client and pprint to prinit data in format.
import pymongo
from pymongo import MongoClient
from pprint import pprint

#username and password for authentic log in.
u='aacuser'
p='12588521'

class AnimalShelter:
    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/AAC'%(u, p))
        # where xxxxx is your unique port number
        self.database = self.client['AAC']

    #Read entire database without taking parameter
    def read_All(self):
            value=self.database.animals.find()
            return value

    #Read specific database
    def read(self,value):
        x=self.database.animals.find(value)
        return x
