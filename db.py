from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId


username = "ijass"
password = "sYWtm6bA2X5UBm8F"

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

# filter = {"title" : 1}

# data = list(tasks.find({}).sort("title", -1))

# completed_Tasks = list(tasks.find({"status" : "pending"}))

# for i in completed_Tasks:
#     print("------------------------")
#     print("Id: ", i["_id"])
#     print("Title: ", i["title"])
#     print("Status: ", i["status"])


# data = tasks.find_one({"_id" : ObjectId("6707b150e8007e634f5d4742")})

# print(data)

# Create

# tasks.insert_one({"title" : "complete python class", "status" : "pending"})
# tasks.insert_many(
#     [
#         {"title" : "Task 2", "status" : "pending"}, 
#         {"title" : "Task 3", "status" : "completed"}
#     ])

# Update
# tasks.update_one({"_id" : ObjectId("67d2d0d81c693f69cb0f804c")}, {"$set" : {"status" : "completed"}})
# tasks.update_many({"status" : "completed"}, {"$set" : {"status" : "pending"}})

#Delete
# tasks.delete_one({"_id" : ObjectId("678bb99937e8ecef4d5ceafc")})
# tasks.delete_many({"status" : "completed"})
# tasks.delete_many({})  !!!! Delete document with concise !!!!

# tasks.drop() # Delete the collection