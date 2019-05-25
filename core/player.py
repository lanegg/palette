# -*- coding: utf-8 -*-

"""
palette player

基本mpv实现
只用其基础播放功能
playlist外置

"""

import logging
import mpv
from enum import IntEnum

logger = logging.getLogger(__name__)


class State(IntEnum):
    """
    Player states.
    """
    stopped = 0
    paused = 1
    playing = 2


class MusicPlayer():

    def __index__(self):
        self.player = mpv.MPV(ytdl=True,
                              input_default_bindings=True,
                              input_vo_keyboard=True)

