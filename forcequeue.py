# Client id: 3c9b472a82084d869ed269f150194d7f
import requests as r
import webbrowser
import os
import base64
from urllib.parse import urlencode
import json


c_id = "3c9b472a82084d869ed269f150194d7f"
c_secret = "2cd1a32207bf4e9e8c77ed96c9a0bd7d"
# You could use base64 to make the authorization basic key but you can also use requests' built-in auth


# # Manually making the header just to prove I can
# # String must be concatenated before base64ing, I was having trouble here because I just can't read the requested header format correctly
# head = base64.standard_b64encode((c_id + ":" + c_secret).encode())
# alt = {"Authorization": "Basic {}".format(head.decode())}
# params = {'grant_type' : "client_credentials"}
# response = r.post("https://accounts.spotify.com/api/token", data=params, headers= alt)


# requests' builtins method for getting the auth key
body_params = {'grant_type' : "client_credentials"}
response=r.post("https://accounts.spotify.com/api/token", data=body_params, auth = (c_id, c_secret))
response = response.json() # Convert the response into a dictionary to get the key
token = "Bearer {}".format(response['access_token'])







# Reading playlist track list
# Medlytics playlist URL: 0WdFaOT7fFVBYSo86tT7mA
# playlistLink = "0WdFaOT7fFVBYSo86tT7mA"

playlistLink = "66t8rUNJJsOMExmrXWH2hC"
playlist = r.get("https://api.spotify.com/v1/playlists/" + playlistLink, headers={"Authorization": token,
                                                                                  "scopes": "playlist-modify-public"})
# print(playlist.json()['tracks']) # Get Tracklist just to test it out






# Have to get user auth in order to modify public playlists, use a flask endpoint
url = "https://accounts.spotify.com/authorize"
urlstuff = urlencode({"client_id":c_id,
            "response_type":"token",
            "redirect_uri":'http://127.0.0.1:5000/spotify/callback',
            "scope":"playlist-modify-public"})
url = url + '?' + urlstuff

# # Gotta manually launch and grab the token, sorry i'm bad at callbacks.
from flask import Flask
app = Flask(__name__)
@app.route("/spotify/callback")
def spotify_callback():
    print("YEA")
    return "You finally called me back!"

webbrowser.open(url)


access = "Bearer {}".format("BQBIJEVs5q5a47UmPFtbETERenrh8HmPvw-W8_Z0OsbTQhoL9yJtWmq61D8oPCQw4vJv1gIBdV7aaR0wPi-HsHaW0NWOM8_GCT5gVFTDmKhP0KQcwoiwTqnLj8YtkQP3iQiszq7Ovhs_lMY5MywPA-M2Bv5KCp1XfpySx108MJGUwcBIYylHTnICPO8")

uris = "spotify:track:2xLjorF0M6LHPqk2qmZJOV"
mhm = r.post("https://api.spotify.com/v1/playlists/" + playlistLink + "/tracks", headers={"Authorization": access,
                                                                                      "Content-Type": "application/json"}
                                                                           , data=json.dumps({"uri":uris}))


# uris = ""
# for i in range(99):
#     uris += "spotify:track:2xLjorF0M6LHPqk2qmZJOV,"
# uris = uris[:-1]
# playlist-modify-public