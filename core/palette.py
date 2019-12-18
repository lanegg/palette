# -*- coding: utf-8 -*-

"""
palette


"""
import sys
import os
from player import MusicPlayer
import library as lib
import processor as processor

import logging

logger = logging.getLogger("__name__")


def palette():

    logger.info("start palette")

    player = MusicPlayer()
    logger.info("player was loaded")

    library = lib.library
    library.load_all_albums()
    logger.info("library was loaded")

    command = ""
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
