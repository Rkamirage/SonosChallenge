import soco
import spotipy

import getpass
from sender import Sender
from find_song_url import SearchEngine


def add_from_service(trackURL, service, device):
    uri = service.sonos_uri_from_id(trackURL)
    res = [DidlResource(uri=uri, protocol_info="DUMMY")]
    didl = DidlItem(title="DUMMY",
        parent_id="DUMMY",  
        item_id=didl_item_id,
        desc=service.desc,
        resources=res)

    device.add_to_queue(didl)


# init receiver
user = input(' - Please enter your gmail account: ')
password = getpass.getpass(' - Please enter your password: ')
friend_email = input(' - Please enter your friends gmail account: ')
client = Sender(user=user, password=password, send_to=friend_email, subject_prefix='Sonos sends you a song')


device = soco.discovery.any_soco()
service = MusicService("Spotify")
song = input("Enter the song you want to play: ")
# search song
url = SearchEngine().search_track(song)
# send song
client.send(url)

add_from_service(url,service,device)
device.play()
