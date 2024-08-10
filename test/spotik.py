import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Ініціалізація клієнта
client_id = '6a810664ce804ca8a1d2b31374a4ec0a'
client_secret = '557be9235aff494593ab7f5dca52ab92'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Функція для отримання треків з плейлиста
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

# Отримання треків з плейлиста
playlist_id = '2oHkKiDU77UwuDIb2LXzuW'
tracks = get_playlist_tracks(playlist_id)

# Виведення треків та їх популярності
for item in tracks:
    track = item['track']
    print(f"Track: {track['name']} - Popularity: {track['popularity']}")

# Примітка: точна кількість прослуховувань через API недоступна
