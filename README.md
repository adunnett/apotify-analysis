# spotify-analysis
## Spotify app
Through the Spotify Web API, external applications retrieve Spotify content such as album data and playlists. To use the API we registered out application with Spotify through the developer space, doing this gave us our client_id and client_secret which are our API keys.

## Spotipy - library
Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy you get full access to all of the music data provided by the Spotify platform.

We first defined a function to obtain the track IDs from a playlist, using the playlist_id. The track ID's hold information such as the name, album, artist etc.
Next, we defined a  function that obtains the features of the tracks in the playlist with a return statement to end the execution of the function call.
We then used a for loop and appended track features to a list then combined it with the track information. This was put into a dataframe and exported to CSVs.

# Definitions

Acousticness value: how acoustic a song is

Danceability value: how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity

Liveness value: the probability that the song was recorded with a live audience

Energy value: represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy

Instrumentalness value: predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content.

Loudness value: shows how loud music is.

Speechiness value: detects the presence of spoken words in a track.

References:
https://towardsdatascience.com/cluster-your-liked-songs-on-spotify-into-playlists-of-similar-songs-66a244ba297e
https://github.com/mari-linhares/spotify-flask
