from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
import json 
import user

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/aimnet"
mongo = PyMongo(app)

@app.route('/login',methods=["POST"])
def login_route():
    data = request.get_json()
    print(data)
    return user.login(data["email"],data["pass1"],mongo)  

@app.route('/signup',methods=["POST"])
def signup_route():
    data = request.get_json()
    print(data)
    return user.signup(data["email"],data["pass1"],data["pass2"],mongo)   
    
if  __name__ == "__main__":
    app.run(debug=True)