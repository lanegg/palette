# -*- coding: utf-8 -*-

"""
palette player

基本mpv实现
只用其基础播放功能
playlist外置

"""

import logging
import lib.mpv as mpv
import os

logger = logging.getLogger(__name__)

class MusicPlayer():

    def __init__(self):
        self.mpv_player = mpv.MPV(ytdl=True,
                              input_default_bindings=True,
                              input_vo_keyboard=True)
        self.mpv_player._event_callbacks.append(self.on_event)
        self.playlist_current = 0
        self.playlist = []

    def play(self):
        song = self.current_song()
        logging.info("try to play {}".format(song))
        self.mpv_player.playlist_clear()
        self.mpv_player.play(song)
        self.mpv_player.pause = False


    def load(self, playlist):
        try:

            if (playlist is not None and len(playlist) > 0):
                logging.info("try load playlist")
                # self.player.pause = True
                self.mpv_player.pause = True
                self.playlist = playlist
                self.play()
            else:
                logging.error("load empty playlist")
        except:
            print("load error")

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
        self.mpv_player.pause = True
        self.playlist_current_changed("next")
        self.play()

    def pre(self):
        self.mpv_player.pause = False
        self.playlist_current_changed("pre")
        self.play()

    def pause(self):
        if (self.mpv_player.pause) :
            self.mpv_player.pause = False
        else:
            self.mpv_player.pause = True

    def on_event(self, event):
        if event['event_id'] == mpv.MpvEventID.END_FILE:
            reason = event['event']['reason']
            logger.debug("current song finished. reason: {}".format(reason))
            if reason != mpv.MpvEventEndFile.ABORTED:
                self.next()