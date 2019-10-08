import soco
import easygui as g
import spotipy
import easygui as g

import getpass
import time
from receiver import Receiver

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
client = Receiver(user, password)
# search for email
song_from_friends = False
while not song_from_friends:
    song_from_friends = client.check_mailbox("Sonos sends")
    time.sleep(10)  # sleep for a while

# init soco device
device = soco.discovery.any_soco()
service = MusicService("Spotify")
add_from_service(song_from_friends, sservice, device)

answer = g.buttonbox(msg = "Do you want to play %s?"%song_from_friends, title="Sonos instant play",
                     choices=['yes', 'no'])
if answer == 'yes':
    print("Enjoy")
    device.play()
