from flask import Flask,jsonify
from flask_pymongo import PyMongo
import json 

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/aimnet"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    users = mongo.db.users.find()
    ul = [] 
    for doc in users:
        print(doc)
        ul.append(doc)
        
    return jsonify({"li":json.dumps(ul, default=str)})


if  __name__ == "__main__":
    app.run(debug=True)