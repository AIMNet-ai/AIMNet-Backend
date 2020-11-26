from flask import jsonify
import json
import random

#Get Profile by Email
def getProfile(email,mongo):
    getter = mongo.db.users.find_one({"email":email})
    #if user is not present in DB
    getter["password"] = None
    if getter is None:
        return jsonify({
            "err":f'No user exists with email {email}'
        })
    else:
        return json.dumps(getter, default=str)

#Update Profile by Email
def updateProfile(email,obj,mongo):
    getter = mongo.db.users.find_one({
        "email": email,
    })
    mongo.db.users.update_one({
    '_id': getter["_id"]
    },{
    '$set': {
        'name':obj["name"],
        'username':obj["username"],
        'profilePic':obj["profilePic"],
        'bio':obj["bio"]
    }
    }, upsert=False)
    getter = mongo.db.users.find_one({
        "email": email,
    })
    return json.dumps(getter,default=str)