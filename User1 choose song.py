from soco import *
import spotipy
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

device = soco.discovery.any_soco()
service = MusicService("Spotify")
#需要一个spotipy的method把一首歌的spotify URL找到
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

song = input("Enter the song you want to play: ")
#通过spotipy的method找到URL
add_from_service(URL,service,device)
device.play()
