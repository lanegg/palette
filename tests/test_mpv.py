# -*- coding: utf-8 -*-
import lib.mpv as mpv
import time

player = mpv.MPV(ytdl=True,
                 input_default_bindings=True,
                 input_vo_keyboard=True)
player.play('/data/code/palette/data/a.mp3')

while True:
    time.sleep(10)
    player.pause = True
    time.sleep(5)
    player.pause = False

