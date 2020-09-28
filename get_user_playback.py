import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


""" TODO: create a spotify API client
then call current_playback()
    get information about user's current playback
"""
cid = "xx"
secret = "xx"
username = "cool23dude"

client_credentials_manager = SpotifyClientCredentials('SPOTIFY_CLIENT_ID', 'SPOTIFY_CLIENT_SECRET')

##https://stackoverflow.com/questions/47379411/invalid-client-when-trying-to-use-spotipy-to-authorize-an-api-call
##was copying from here
scope = 'user-read-currently-playing user-read-playback-state'

token = util.prompt_for_user_token(username,scope,
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
user = sp.user('cool23dude')
print(user)



#https://github.com/plamere/spotipy/issues/194
