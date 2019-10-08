from soco import *
import easygui as g
import spotipy
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import easygui as g

from receiver import Receiver

device = soco.discovery.any_soco()
service = MusicService("Spotify")
#从user1的sonos app发过来URL
string track_id
def add_from_service(trackURL, service, device):
    uri = service.sonos_uri_from_id(trackURL)
    res = [DidlResource(uri=uri, protocol_info="DUMMY")]
    didl = DidlItem(title="DUMMY",
        parent_id="DUMMY",  
        item_id=didl_item_id,
        desc=service.desc,
        resources=res)

    device.add_to_queue(didl)


add_from_service(URL,service,device)

answer = g.buttonbox(msg = "Do you want to play the song?", title="Sonos instant play",
                     choices=['yes', 'no'])
if answer == 'yes':
    print("Enjoy")
    device.play()
