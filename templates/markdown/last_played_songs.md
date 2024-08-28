<table style="border: none; padding: 20px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); max-width: 100%; font-family: Arial, sans-serif;">
  <tr>
    <td colspan="3" style="padding-bottom: 10px;">
      <h4 style="margin: 0; font-size: 12px; color: black;">Last <a href="{{ user_page_url }}">{{ username }}</a> played songs</h4>
    </td>
  </tr>

  <!-- Begin song rows -->
  {% for song in recent_songs %}
  <tr style="border-bottom: 1px solid #ddd;">
    <td style="padding: 10px 10px 10px 0;">
      <img src="{{ song['track']['album']['images'][0]['url'] }}" href="{{ song['track']['external_urls']['spotify'] }}" alt="Album cover" style="width: 60px; height: 60px;">
    </td>
    <td style="vertical-align: top; padding-left: 10px;">
      <p style="margin: 0; color: black;"><a href="{{ song['track']['external_urls']['spotify'] }}"><strong>{{ song['track']['name'] }}</strong></a></p>
      <p style="margin: 5px 0 0 0; color: grey;">{{ format_authors(song['track']['artists'],include_urls=True) }}</p>
    </td>
  </tr>
  {% endfor %}
  <!-- End song rows -->
</table>