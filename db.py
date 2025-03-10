
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

data = list(tasks.find({}, {"_id": 0, "title" : 1}).sort("title", -1))

print(data)

# completed_Tasks = list(tasks.find({"status" : "completed"}))

# data = tasks.find_one({"_id" : ObjectId("6707b150e8007e634f5d4742")})

# print(completed_Tasks)