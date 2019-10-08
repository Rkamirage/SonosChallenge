import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

class SearchEngine:
	def __init__(self):
		# account info
		CLIENT_ID = '5a6b2e6c45524fd590ae6dae67266efe'
		CLIENT_SECRET = '015a05f6432348e0949e12c210b2becb'

		# init client
		client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
		self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	# search
	def search_artist(self, artist):
		results = self.sp.search(q='artist:'+artist, type='artist')

		return(results['artists']['items'][0]['uri'])

	def search_track(self, track):
		results = self.sp.search(q='track:'+track, type='track')

		return(results['tracks']['items'][0]['uri'])
