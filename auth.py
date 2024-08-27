from flask import Flask, request, jsonify
from spotipy.oauth2 import SpotifyOAuth
app = Flask(__name__)
import os

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

scopes = [
    'user-library-read',
    'user-read-playback-position',
    'user-top-read',
    'user-read-recently-played',
    'user-follow-read',
    'user-read-currently-playing',
    ]

auth = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri='http://localhost:5000',scope=scopes)

print(auth.get_authorize_url())

@app.route('/', methods=['GET'])
def home():
    code = request.args.get('code')

    return jsonify(auth.get_access_token(code))



if __name__ == '__main__':
    app.run(port=5000)