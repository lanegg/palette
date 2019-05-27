import core.player as music_player
import time

player = music_player.mp

playlist = ["/data/code/palette/data/a.mp3", "/data/code/palette/data/b.mp3", "/data/code/palette/data/c.mp3"]
player.load(playlist)

while True:
    time.sleep(10)
    player.pause()
