from soco import *
import spotipy
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

device = soco.discovery.any_soco()
service = MusicService("Spotify")
song = input("Enter the song you want to play: ")
# search song
url = SearchEngine().search_track(song)

add_from_service(url,service,device)
device.play()
