
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


username = "enter your username"
password = "enter your password"

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

data = list(tasks.find())

print(data)