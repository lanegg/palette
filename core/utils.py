# -*- coding: utf-8 -*-

import logging
import os
import yaml



#root path
root_path = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))

#logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filemode='w')

#config json
with open(root_path + "/palette.yml", encoding='UTF-8') as config_file:
    config = yaml.load(config_file)

