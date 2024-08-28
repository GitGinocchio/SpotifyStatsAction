<table style="border: none; padding: 20px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); max-width: 100%; font-family: Arial, sans-serif;">
  <tr>
    <td colspan="3" style="padding-bottom: 10px;">
      <h4 style="margin: 0; font-size: 12px; color: black;">Top Artists of <a href="{{ user_page_url }}">{{ username }}</a></h4>
    </td>
  </tr>

  <!-- Begin artist rows -->
  {% for artist in top_artists %}
  <tr style="border-bottom: 1px solid #ddd;">
    <td style="padding: 10px 10px 10px 0;">
      <img src="{{ artist['images'][0]['url'] }}" href="{{ artist['external_urls']['spotify'] }}" alt="Artist image" style="width: 60px; height: 60px;">
    </td>
    <td style="vertical-align: top; padding-left: 10px;">
      <p style="margin: 0; color: black;"><a href="{{ artist['external_urls']['spotify'] }}"><strong>{{ artist['name'] }}</strong></a></p>
      <p style="margin: 5px 0 0 0; color: grey;">{{ artist['genres'] | join(', ') }}</p>
    </td>
    <td style="vertical-align: top; padding-left: 10px;">
      <p style="margin: 0; color: black;">Popularity: <strong>{{ artist['popularity'] }}%</strong></p>
    </td>
  </tr>
  {% endfor %}
  <!-- End artist rows -->
</table>