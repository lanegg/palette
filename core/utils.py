# -*- coding: utf-8 -*-

import logging
import os
import yaml

#root path
root_path = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
#config json
with open(root_path + "/palette.yml", encoding='UTF-8') as config_file:
    config = yaml.load(config_file)