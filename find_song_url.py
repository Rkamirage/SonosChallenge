import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# account info
CLIENT_ID = '5a6b2e6c45524fd590ae6dae67266efe'
CLIENT_SECRET = '015a05f6432348e0949e12c210b2becb'

# init client
client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# search
def search_artist(artist):
	results = sp.search(q='artist:'+artist, type='artist')

	return(results['artists']['items'][0]['uri'])

def search_track(track):
	results = sp.search(q='track:'+track, type='track')

	return(results['tracks']['items'][0]['uri'])
	# return results['artists']['items'][0]['uri']

search_track('south of the boarder')