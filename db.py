
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId


username = "Enter your username"
password = "Enter your password"

uri = f"mongodb+srv://{username}:{password}@students.jooqal4.mongodb.net/?retryWrites=true&w=majority&appName=STUDENTS"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["TODO"]

tasks = db["tasks"]

# CRUD

# Read

# data = list(tasks.find({}, {"_id": 0, "title" : 1}).sort("title", -1))

# print(data)

# completed_Tasks = list(tasks.find({"status" : "completed"}))

# data = tasks.find_one({"_id" : ObjectId("6707b150e8007e634f5d4742")})

# print(completed_Tasks)

# Create

# tasks.insert_one({"title" : "Task 1", "status" : "pending"})
# tasks.insert_many([{"title" : "Task 2", "status" : "pending"}, {"title" : "Task 3", "status" : "completed"}])

# Update
# tasks.update_one({"_id" : ObjectId("678bbc7de80b960cd7ebd29a")}, {"$set" : {"status" : "pending"}})
# tasks.update_many({"status" : "pending"}, {"$set" : {"status" : "completed"}})