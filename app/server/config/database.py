from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient()

db = client['gcp-poc-db']
products_collection = db['products']