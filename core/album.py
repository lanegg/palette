# -*- coding: utf-8 -*-

"""
album
"""

import logging
import os
import core.processor as processor
import core.utils as utils


class Album():

    def __init__(self, path):
        self.path = path
        self.songs = []

    def initialization(self):
        logging.info("try to initialization album {}".format(self.path))
        self.cover_path = os.path.join(self.path, "cover.jpg")
        self.load_songs()
        self.features = processor.build_features(self.cover_path)

    def load_songs(self):
        files = os.listdir(self.path)
        for file in files:
            for suffix in utils.config["media_types"]:
                if file.endswith(suffix):
                    self.songs.append(os.path.join(self.path, file))

    def is_not_empty(self):
        return self.songs is not None and len(self.songs) > 0
