import requests 

url = "http://127.0.0.1:5000/api/predictPopularity"

# request.get(url)


data = {
    "Length": 175255,
    "Acousticness": 0.00223, 
    "Danceability": 0.806, 
    "Energy": 0.869, 
    "Instrumentalness": 0.775000, 
    "Liveness": 0.1230,
    "Loudness": -4.344,
    "Speechiness": 0.0544,
    "Tempo": 124.010
}

response = requests.post(url, json=data)
print(response.text)