# -*- coding: utf-8 -*-

"""
音乐库管理
基于远程目录挂载
"""

import logging
import os
import album as album
import processor as processor
import utils as utils

logger = logging.getLogger(__name__)



class Library():

    def __init__(self):
        self.albums = {}

    def load_all_albums(self):

        for maindir, subdir, file_name_list in os.walk(utils.config["media_path"]):
            # list all media
            for filename in file_name_list:
                # find cover
                if 'cover.jpg' == filename:
                    _album = album.Album(maindir)
                    _album.initialization()
                    self.albums[maindir] = _album



library = Library()
