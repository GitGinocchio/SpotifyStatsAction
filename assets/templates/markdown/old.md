### Last Update Timestamp
<p>{timestamp.strftime("%d/%m/%Y, %H:%M:%S")}</p>

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