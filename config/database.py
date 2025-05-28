from pymongo import MongoClient

client=MongoClient("mongodb+srv://praveenbyju:Praveen1999@cluster0.ltcoe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client.todo_db

collection_name=db["todo_collection"]