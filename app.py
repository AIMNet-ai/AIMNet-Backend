from flask import Flask,jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/aimnet"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    users = mongo.db.users.find()
    for doc in users:
        print(doc)
    return 'fuck hi bye World!'


if  __name__ == "__main__":
    app.run(debug=True)