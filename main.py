from spotipy.oauth2 import SpotifyOAuth
import requests
import spotipy
import base64
import os

# Sostituisci con le tue credenziali
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

auth = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri='http:/localhost:5000',scope=scopes,cache_path=os.devnull)

token_info = auth.refresh_access_token(REFRESH_TOKEN)

sp = spotipy.Spotify(auth=token_info['access_token'],oauth_manager=auth)



# Ottieni i top artisti e top canzoni
top_artists = sp.current_user_top_artists(limit=10)['items']
top_tracks = sp.current_user_top_tracks(limit=10)['items']
recent_tracks = sp.current_user_recently_played(limit=10)['items']



svg_content = f"""
<svg width="500" height="250" xmlns="http://www.w3.org/2000/svg" version="1.1">
  <!-- Background -->

  <!-- Contenitore con angoli arrotondati -->
  <rect x="10" y="10" width="480" height="230" rx="20" ry="20" fill="#34495e" />

  <!-- Album Cover -->
  <clipPath id="clip-circle">
    <circle cx="125" cy="125" r="100" />
  </clipPath>
  <image href="{recent_tracks[0]['track']['album']['images'][0]['url']}" width="250" height="250" clip-path="url(#clip-circle)" />

  <!-- Title -->
  <text x="250" y="100" font-family="Arial" font-size="45" fill="white">{recent_tracks[0]["track"]["name"].capitalize()}</text>

  <!-- Artist -->
  <text x="250" y="150" font-family="Arial" font-size="24" fill="white">Artist: {recent_tracks[0]['track']['album']['artists'][0]['name']}</text>
</svg>
"""

# Salva il file SVG
with open("latest_track.svg", "w") as f:
    f.write(svg_content)