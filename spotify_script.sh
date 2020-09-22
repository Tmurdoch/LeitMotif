
#!/bin/sh
set -x
#purpose: call spotify for request (and access to user data) 
#and get current song name + title, etc.,
#output should be pipelinable


#use implicit grant flow method
#https://stackoverflow.com/questions/31092808/is-it-possible-to-use-the-spotify-web-api-to-write-a-desktop-application-without

#GET https://accounts.spotify.com/authorize?client_id=5fe01282e44241328a84e7c5cc169165&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-read-private%20user-read-email&state=34fFs29kd09

GET https://accounts.spotify.com/authorize?client_id=a211de10b38d44b1a4874a0d4281a8aa&response_type=code&redirect_uri=my-awesome-app-login://callback&scope=user-read-playback-state


export SPOTIPY_CLIENT_ID= 'a211de10b38d44b1a4874a0d4281a8aa'
export SPOTIPY_CLIENT_SECRET= 'de03be8b50074a55a92e1d97c68ea498'
export SPOTIPY_REDIRECT_URI= 'http://localhost'

#TODO: run python script

python get_user_playback.py

#TODO: cat this to an html file, then open it in a browser, sign in wait for response
#TODO: figure out what to do after recieving token, or after recieving song name and artist
