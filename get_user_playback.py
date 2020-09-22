import spotipy



""" TODO: create a spotify API client
then call current_playback()
    get information about user's current playback
"""

sp = spotipy.Spotify()
user = sp.user('cool23dude')
print(user)

