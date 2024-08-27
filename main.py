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
<svg width="1200" height="500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
  <!-- Background with rounded corners -->
  <defs>
    <clipPath id="rounded-clip">
      <rect x="0" y="0" width="1200" height="500" rx="20" ry="20"/>
    </clipPath>
    <!-- Clip paths for rounded images -->
    <!--
    <clipPath id="circle-clip">
      <circle cx="30" cy="30" width="30" height="30" r="90"/>
    </clipPath>
    -->
  </defs>



  <!-- Background -->
  <rect width="100%" height="100%" fill="#2c3e50" clip-path="url(#rounded-clip)"/>

  <!-- Sezione Top Artists -->
  <g fill="white" font-family="Arial" font-size="20" clip-path="url(#rounded-clip)">
    <text x="20" y="40" font-size="30" font-weight="bold" fill="white">Top 10 Artists:</text>
    {''.join([
        f'<a xlink:href="{artist["external_urls"]["spotify"]}" target="_blank">'
        f'<image x="10" y="{80 + i * 40}" width="30" height="30" xlink:href="{artist["images"][0]["url"]}" clip-path="url(#circle-clip)"/>'
        f'<text x="50" y="{100 + i * 40}" font-size="20" fill="white" width="250" overflow="visible">{artist["name"]}</text>'
        f'</a>'
        for i, artist in enumerate(top_artists)
    ])}
  </g>

  <!-- Separatore -->
  <line x1="340" y1="20" x2="340" y2="1000" stroke="white" stroke-width="2" clip-path="url(#rounded-clip)"/>

  <!-- Sezione Top Tracks -->
  <g fill="white" font-family="Arial" font-size="20" clip-path="url(#rounded-clip)">
    <text x="360" y="40" font-size="30" font-weight="bold" fill="white">Top 10 songs:</text>
    {''.join([
        f'<a xlink:href="{track["external_urls"]["spotify"]}" target="_blank">'
        f'<image x="360" y="{80 + i * 40}" width="30" height="30" xlink:href="{track['album']['images'][0]['url']}" clip-path="url(#circle-clip)"/>'
        f'<text x="400" y="{100 + i * 40}" font-size="20" fill="white" width="250" overflow="visible">{track["name"]}</text>'
        f'</a>'
        for i, track in enumerate(top_tracks)
    ])}
  </g>

  <!-- Separatore -->
  <line x1="680" y1="20" x2="680" y2="1000" stroke="white" stroke-width="2" clip-path="url(#rounded-clip)"/>

  <!-- Sezione Recent Tracks -->
  <g fill="white" font-family="Arial" font-size="20" clip-path="url(#rounded-clip)">
    <text x="700" y="40" font-size="30" font-weight="bold" fill="white">Last 10 Songs Listened To:</text>
    {''.join([
        f'<a xlink:href="{track["track"]["external_urls"]["spotify"]}" target="_blank">'
        f'<image x="700" y="{80 + i * 40}" width="30" height="30" xlink:href="{track['track']['album']['images'][0]['url']}" clip-path="url(#circle-clip)"/>'
        f'<text x="740" y="{100 + i * 40}" font-size="20" fill="white" width="250" overflow="visible">{track["track"]["name"]}</text>'
        f'</a>'
        for i, track in enumerate(recent_tracks)
    ])}
  </g>
</svg>
"""

# Salva il file SVG
with open("latest_track.svg", "w") as f:
    f.write(svg_content)