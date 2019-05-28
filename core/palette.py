# -*- coding: utf-8 -*-

"""
palette


"""

import logging
from core.player import MusicPlayer
import core.library as lib
import core.processor as processor


def palette():

    player = MusicPlayer()
    command = ""

    library = lib.library
    library.load_all_albums()

    while command != "quit":

        if command == "load":
            album = processor.scan()
            player.load(album)

        if command == "pause":
            player.pause()

        if command == "next":
            player.next()

        if command == "pre":
            player.pre()

        command = input("command:")


if __name__ == '__main__':
    palette()