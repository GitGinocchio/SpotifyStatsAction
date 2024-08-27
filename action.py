from spotipy.oauth2 import SpotifyOAuth
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

# Nuovo contenuto da inserire nella sezione
new_content = f"""
### Last Update Timestamp
<p>{datetime.datetime.now(datetime.UTC).strftime("%d/%m/%Y, %H:%M:%S")}</p>

<!--- Inizia la sezione estendibile per i Top Artists --->
<details open>
  <summary style="font-size: 20px; font-weight: bold; cursor: pointer; text-align: center;">Top 10 Artists</summary>
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 10px;">
    {''.join([
      f'<a href="{artist["external_urls"]["spotify"]}" target="_blank" style="text-decoration: none; color: #000; display: flex; flex-direction: column; align-items: center; text-align: center;">'
      f'<img src="{artist["images"][0]["url"]}" alt="{artist["name"]}" style="width: 80px; height: 80px; margin-bottom: 5px;" />'
      f'<p style="font-size: 16px; font-weight: bold; color: #000; margin: 0;">{artist["name"]}</p>'
      f'</a>'
      for artist in top_artists
    ])}
  </div>
</details>

<!--- Inizia la sezione estendibile per le ultime 10 canzoni ascoltate --->
<details open>
  <summary style="font-size: 20px; font-weight: bold; cursor: pointer; text-align: center;">Last 10 Songs Listened To</summary>
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 10px;">
    {''.join([
      f'<a href="{track["track"]["external_urls"]["spotify"]}" target="_blank" style="text-decoration: none; color: #000; display: flex; flex-direction: column; align-items: center; text-align: center;">'
      f'<img src="{track["track"]["album"]["images"][0]["url"]}" alt="{track["track"]["name"]}" style="width: 80px; height: 80px; margin-bottom: 5px;" />'
      f'<p style="font-size: 16px; font-weight: bold; color: #000; margin: 0;">{track["track"]["name"]}</p>'
      f'</a>'
      for track in recent_tracks
    ])}
  </div>
</details>

<!--- Inizia la sezione estendibile per le 10 canzoni più ascoltate --->
<details open>
  <summary style="font-size: 20px; font-weight: bold; cursor: pointer; text-align: center;">Top 10 Most Played Songs</summary>
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 10px;">
    {''.join([
      f'<a href="{track["external_urls"]["spotify"]}" target="_blank" style="text-decoration: none; color: #000; display: flex; flex-direction: column; align-items: center; text-align: center;">'
      f'<img src="{track["album"]["images"][0]["url"]}" alt="{track["name"]}" style="width: 80px; height: 80px; margin-bottom: 5px;" />'
      f'<p style="font-size: 16px; font-weight: bold; color: #000; margin: 0;">{track["name"]}</p>'
      f'</a>'
      for track in top_tracks
    ])}
  </div>
</details>
"""

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