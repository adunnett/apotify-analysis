from flask import Flask, redirect, request, jsonify, abort, render_template
import startup
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib
import urllib
import time


app = Flask(__name__)

# LOAD MODEL 
random_forest = joblib.load('random_forest_updated.smd')
predictMood = joblib.load('moodClassification.smd') # load model 

@app.route('/')
def index():
    response = startup.getUser()
    return redirect(response)

@app.route('/callback/')
def callback():
    startup.getUserToken(request.args['code'])
    return render_template('index.html')


@app.route('/api/predictPopularity', methods=["GET", "POST"])
def predictPopularity(): 

    time.sleep(1)

    # IF 'GET', THEN PROVIDE API DOCS 
    if request.method == "GET": 
        return "Here's some info on how use my API... " # render_template("apiDocs.html") 

    if not request.json: 
        abort(400) # special function that returns a 400 error page 

    # IF 'POST', THEN PERFORM PREDICTION AND RETURN PREDICTED RESULT 
    input_json = {
        "Length": request.json["Length"],
        "Acousticness": request.json["Acousticness"],
        "Danceability": request.json["Danceability"],
        "Energy": request.json["Energy"],
        "Instrumentalness": request.json["Instrumentalness"],
        "Liveness": request.json["Liveness"],
        "Loudness": request.json["Loudness"],
        "Speechiness": request.json["Speechiness"],
        "Tempo": request.json["Tempo"]
    }

    input_values = np.fromiter(input_json.values(), dtype=float)   # [value1, value2, value3..... ]
    print(input_values) 
    predicted_values = random_forest.predict([input_values])[0]
    return jsonify({"prediction": str(predicted_values)})


@app.route('/api/predictMood', methods=["GET", "POST"])
def predictMood(): 

    # IF 'GET', THEN PROVIDE API DOCS 
    if request.method == "GET": 
        return "Here's some info on how use my API... " # render_template("apiDocs.html") 

    if not request.json: 
        abort(400) # special function that returns a 400 error page 

    # IF 'POST', THEN PERFORM PREDICTION AND RETURN PREDICTED RESULT 
    input_json = {
        "Danceability": request.json["Danceability"],
        "Energy": request.json["Energy"],
        "Loudness": request.json["Loudness"],
        "Valence": request.json["Valence"],
        "Tempo": request.json["Tempo"]
    }

    input_values = np.fromiter(input_json.values(), dtype=float)   # [value1, value2, value3..... ]
    print(input_values) 
    predicted_values = predictMood.predict([input_values])[0]
    return jsonify({"prediction": str(predicted_values)})

@app.route('/playlists')
def getSongs():
    url = "https://api.spotify.com/v1/me/playlists"
    header = {
        "Authorization": f"Bearer {startup.getAccessToken()[0]}"
    }
    response = requests.get(url, headers=header)
    return jsonify(response.json())

@app.route('/artists')
def getArtists():
    url = "https://api.spotify.com/v1/me/top/artists"
    header = {
        "Authorization": f"Bearer {startup.getAccessToken()[0]}"
    }
    response = requests.get(url, headers=header)
    return jsonify(response.json())

@app.route('/recent')
def getRecent():
    url = "https://api.spotify.com/v1/me/player/recently-played?limit=10/"
    header = {
        "Authorization": f"Bearer {startup.getAccessToken()[0]}"
    }
    response = requests.get(url, headers=header)
    return jsonify(response.json())

@app.route('/api/getSong/<songName>')
def getSong(songName):
    songName_encoded = urllib.parse.quote(songName)
    searchUrl = f"https://api.spotify.com/v1/search?q={songName_encoded}&type=track"

    header = {
        "Authorization": f"Bearer {startup.getAccessToken()[0]}"
    }
  
    searchResponse = requests.get(searchUrl, headers=header)
    track_id = searchResponse.json()["tracks"]["items"][0]["id"]
    audio_feature_url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    audio_feature_response = requests.get(audio_feature_url, headers=header)

    return jsonify(audio_feature_response.json())



@app.route('/api/getArtist/<songName>')
def getArtist(songName):

    songName_encoded = urllib.parse.quote(songName)
    searchUrl2 = f"https://api.spotify.com/v1/search?q={songName_encoded}&type=track"
    header = {
        "Authorization": f"Bearer {startup.getAccessToken()[0]}"
    }
    searchResponse2 = requests.get(searchUrl2, headers=header)
    track_id2 = searchResponse2.json()["tracks"]["items"][0]["id"]
    artist_url = f"https://api.spotify.com/v1/tracks/{track_id2}"
    artist_response = requests.get(artist_url, headers=header)
    return jsonify(artist_response.json())



# HTML PAGES
@app.route('/forest')
def forest():
    return render_template('forest.html')

@app.route('/mood')
def mood():
    return render_template('mood.html')

@app.route('/clustering')
def clustering():
    return render_template('clustering.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)