# -*- coding: utf-8 -*-

"""
音乐库管理
基于远程目录挂载
"""

import logging
import yaml
import os
import core.utils as utils

logger = logging.getLogger(__name__)

class Library():

    def __init__(self):
        self.covers = []


    def load_all_covers(self):

        for maindir, subdir, file_name_list in os.walk(utils.config["media_path"]):
            # list all media
            for filename in file_name_list:
                # find cover
                if 'cover.jpg' == filename:
                    apath = os.path.join(maindir, filename)
                    self.covers.append(apath)


library = Library()
library.load_all_covers()
print(library.covers)

