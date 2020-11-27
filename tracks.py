from flask import jsonify
import json
import random
from bson.objectid import ObjectId

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

# Toggle favourite flag
def toggleFavTrack(email,id,mongo):
    # writer=''
    # status = False
    # getter = mongo.db.tracks.find({"email":email,"_id":id})
    # for doc in getter:
    #     status = doc["favorite"]
    #     writer = doc.title
    # print(status)
    # print(writer)
    # nostatus = not status
    # updater = mongo.db.tracks.update_one({"email":email,"_id":id},{"$set":{"favorite":nostatus}})
    sts = mongo.db.tracks.find_one({"_id" : ObjectId(id)})
    neg = not sts["favorite"]
    print(sts["favorite"])
    mongo.db.tracks.find_one_and_update(
        {"_id" : ObjectId(id)},
        {"$set":
            {"favorite": neg}
        },upsert=True
    )
    
    if sts is None:
        return jsonify({
            "err":f'Something Went Wrong!'
        })
    else:
        return jsonify({
            "msg":f"Toggled the favourite for song"
        })
  