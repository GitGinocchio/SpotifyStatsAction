from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REFRESH_TOKEN = os.environ['REFRESH_TOKEN']

scopes = [
    'user-library-read',
    'user-read-playback-position',
    'user-top-read',
    'user-read-recently-played',
    'user-follow-read',
    'user-read-currently-playing'
]

def get_spotify():
    auth = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri='http:/localhost:5000',scope=scopes,cache_path=os.devnull)

    token_info = auth.refresh_access_token(REFRESH_TOKEN)

    return spotipy.Spotify(auth=token_info['access_token'],oauth_manager=auth)