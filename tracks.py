from flask import jsonify
import json
import random

# Get all music tracks
def getAllMusicTracks(email,mongo):
    lst = []
    getter = mongo.db.tracks.find({"email":email})
    #if user is not present in DB
    if getter is None:
        return jsonify({
            "err":f'No user exists with email {email}'
        })
    else:
        for doc in getter:
            lst.append(doc)
            print(doc)
        print(lst)
        return json.dumps({"tracks":lst},default=str)
    
    
    
# Get Favourite music tracks
def getFavMusicTracks(email,mongo):
    lst = []
    getter = mongo.db.tracks.find({"email":email,"favorite":True})
    #if user is not present in DB
    if getter is None:
        return jsonify({
            "err":f'No user exists with email {email}'
        })
    else:
        for doc in getter:
            lst.append(doc)
            print(doc)
        print(lst)
        return json.dumps({"tracks":lst},default=str)
  