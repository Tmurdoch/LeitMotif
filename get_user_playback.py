import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



""" TODO: create a spotify API client
then call current_playback()
    get information about user's current playback
"""
client_credentials_manager = SpotifyClientCredentials('SPOTIFY_CLIENT_ID', 'SPOTIFY_CLIENT_SECRET')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
user = sp.user('cool23dude')
print(user)



#https://github.com/plamere/spotipy/issues/194
