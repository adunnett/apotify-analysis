from flask_spotify_auth import getAuth, refreshAuth, getToken

# Add your client ID
CLIENT_ID = "b590b765954445a2860f075ef51d658b"

# aDD YOUR CLIENT SECRET FROM SPOTIFY
CLIENT_SECRET = "07943d05eb414f75883ec7b5d469f127"

# Port and callback url can be changed or ledt to localhost:5000
PORT = "5000"
CALLBACK_URL = "http://localhost"  # http://localhost:5000/callback

# Add needed scope from spotify user
SCOPE = "user-read-private user-read-email playlist-read-private user-top-read user-read-recently-played"
# token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, "{}:{}/callback/".format(CALLBACK_URL, PORT), SCOPE)


def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET,
                          "{}:{}/callback/".format(CALLBACK_URL, PORT))


def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()


def getAccessToken():
    return TOKEN_DATA
