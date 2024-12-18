#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vlc
import time

media_player = vlc.MediaPlayer()
media = vlc.Media("susan_wong_sway.m4a")
media_player.set_media(media)

media_player.play()

#  wait so the media can be played for 1 second 
#  irrespective for length of it.
time.sleep(1)

value = media_player.get_length()
print("Length of the media : ")
print(value)
time.sleep(value/1000)
