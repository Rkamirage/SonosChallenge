# Import soco and get a SoCo instance
import soco
device = soco.discovery.any_soco()

# Get all albums from the music library that contains the word "Black"
# and add them to the queue
albums = device.music_library.get_albums(search_term='Black')
for album in albums:
    print('Added:', album.title)
    device.add_to_queue(album)

# Dial up the volume (just a bit) and play
device.volume += 10
device.play()