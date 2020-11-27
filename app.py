from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
import json 
import user,profile,tracks
# import model_helper
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/aimnet"
mongo = PyMongo(app)

############################################
# User Auth Routes
@app.route('/api/login',methods=["POST"])
def login_route():
    data = request.get_json()
    print(data)
    return user.login(data["email"],data["pass1"],mongo)  

@app.route('/api/signup',methods=["POST"])
def signup_route():
    data = request.get_json()
    print(data)
    return user.signup(data["email"],data["pass1"],data["pass2"],mongo)   

##############################################
# Profile Routes
@app.route('/api/getprofile',methods=["POST"])
def getprofile_route():
    data = request.get_json()
    print(data)
    return profile.getProfile(data["email"],mongo)  

@app.route('/api/updateprofile',methods=["POST"])
def updateprofile_route():
    data = request.get_json()
    print(data)
    return profile.updateProfile(data["email"],data,mongo)   


##############################################
# # Generating Music by notes
# @app.route('/api/generateMusic',methods=["POST"])
# def generateMusic_route():
#     data = request.get_json()
#     return model_helper.genrateMusicByNote(data['note'],data["email"],mongo)  

##############################################
# Get all music tracks of the user
@app.route('/api/getalltracks',methods=["POST"])
def getalltracks_route():
    data = request.get_json()
    print(data)
    return tracks.getAllMusicTracks(data["email"],mongo)   

# Get Favorited music tracks of the user
@app.route('/api/getfavtracks',methods=["POST"])
def getfavtracks_route():
    data = request.get_json()
    print(data)
    return tracks.getFavMusicTracks(data["email"],mongo)   


# Favourite/Unfavourite the tracks
@app.route('/api/toggletracks',methods=["POST"])
def booltrackfav_route():
    data = request.get_json()
    print(data)
    return tracks.toggleFavTrack(data["email"],data["_id"],mongo)   


if  __name__ == "__main__":
    app.run(debug=True)
   