import lstm_model as lstm
import random_name_titles as rn
import json 

# Model predicator
def genrateMusicByNote(note,email,mongo):
    strseq = lstm.generate_sequence(90,note,500)
    print(strseq)
    db_id = mongo.db.tracks.insert_one({
        'musicStr':strseq,
        'title':rn.randomSongName(),
        "favorite":False,
        'email':email
    }).inserted_id
    getter = mongo.db.tracks.find_one({
        "_id": db_id,
    })
    return json.dumps(getter,default=str)