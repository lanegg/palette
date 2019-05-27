# -*- coding: utf-8 -*-

"""
palette player

基本mpv实现
只用其基础播放功能
playlist外置

"""

import logging
import mpv
import os
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
        self.player._event_callbacks.append(self.on_event)
        self.playlist_current = 0
        self.state = State.stopped
        self.playlist = []

    def play(self):
        self.player.playlist_clear()
        self.player.play(self.current_song())
        self.player.pause = False
        self.state = State.playing


    def load(self, playlist):
        if (playlist is not None and len(playlist) > 0):

            # self.player.pause = True
            self.player.pause = True
            self.playlist = playlist
            self.play()

        else:
            return 0




    def current_song(self):
        if self.playlist is not None and len(self.playlist) > 0:
            song = self.playlist[self.playlist_current]

            if (os.path.exists(song)):
                return song
            else:
                logging.error("current song {} is not exists, try next song".format(song))
                self.playlist_current_changed("next")
                return self.current_song()
        else :
            logging.error("playlist is empty")


    def playlist_current_changed(self, opera):
        if self.playlist is not None and len(self.playlist) > 1:
            if "next" == opera:
                if self.playlist_current < len(self.playlist) - 1:
                    self.playlist_current = self.playlist_current + 1
                else:
                    self.playlist_current = 0
            if "pre" == opera:
                if self.playlist_current == 0:
                    self.playlist_current = len(self.playlist) - 1
                else:
                    self.playlist_current = self.playlist_current - 1

    def next(self):
        if self.state == State.playing:
            self.playlist_current_changed("next")
            self.play()

    def pre(self):
        if self.state == State.playing:
            self.playlist_current_changed("pre")
            self.play()


    def on_event(self, event):
        if event['event_id'] == mpv.MpvEventID.END_FILE:
            reason = event['event']['reason']
            logger.debug("current song finished. reason: {}".format(reason))
            if self.state != State.stopped and reason != mpv.MpvEventEndFile.ABORTED:
                self.song_finished.emit()


