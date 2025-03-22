from flask import Flask
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb+srv://Kali_Cluster:swzyYc3c15s6Foee@cluster1.bc6zu.mongodb.net/Practice_1")
db = client["Practice_1"]
collection = db["Students"]

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/add/<name>/<int:age>/<int:score>/<email>")
def add(name, age, score, email):
    collection.insert_one({"name": name, "age": age, "score": score, "email": email})
    return "Added"

@app.route("/find/<name>")
def find(name):
    student = collection.find_one({"name": name})
    if student:
        return f"Name: {student['name']}, Age: {student['age']}, Score: {student['score']}, Email: {student['email']}"
    return "Student not found"

@app.route("/update/<name>/<int:age>/<int:score>/<email>")
def update(name, age, score, email):
    result = collection.update_one({"name": name}, {"$set": {"age": age, "score": score, "email": email}})
    if result.modified_count > 0:
        return "Updated"
    return "No matching record found"

@app.route("/delete/<name>")
def delete(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        return "Deleted"
    return "No matching record found"

if __name__ == "__main__":
    app.run(debug=True)
