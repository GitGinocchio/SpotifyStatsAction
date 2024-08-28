from spotipy.oauth2 import SpotifyOAuth
from utils import *
import requests
import spotipy
import base64
import datetime
import os
import re

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



# Leggi il contenuto del file README.md
with open('README.md', 'r') as file:
    readme_content = file.read()

#timestamp = datetime.timedelta(hours=2) + datetime.datetime.now(datetime.UTC)

# Nuovo contenuto da inserire nella sezione
with open(r"templates\markdown\last_played_song.md",'r') as file:
    new_content = file.read()
    new_content = new_content.format(
      	username=sp.me()['display_name'],
      	song_image_url=recent_tracks[0]["track"]["album"]["images"][0]["url"],
      	song_title=recent_tracks[0]["track"]["name"],
      	song_authors=format_authors(recent_tracks[0]['track']['artists'])
    )

# Usa un'espressione regolare per trovare la sezione e sostituirne il contenuto
updated_content = re.sub(
    r'<!-- START_SECTION: Spotify Stats -->.*?<!-- END_SECTION: Spotify Stats -->',
    f'<!-- START_SECTION: Spotify Stats -->\n{new_content}\n<!-- END_SECTION: Spotify Stats -->',
    readme_content,
    flags=re.DOTALL
)

# Scrivi il contenuto aggiornato nel file README.md
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(updated_content)