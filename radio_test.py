#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  file name : radio_test.py
#  description : This program is a test program for the radio.
#  author : Kibum Park
#  date : 2018. 7. 11.

import time
import serial
import vlc

#  get comport object
ser = serial.Serial('COM10', 9600)

media_player = vlc.MediaPlayer()
media = vlc.Media("test_speech.mp3")

while True:
    # GRD is pin 5
    # DTR is pin 4

    #  push PTT
    ser.dtr = True

    #  and wait for a second
    time.sleep(1)

    #  to make the media replay by setting the media to it's current media and calling play. 
    media_player.set_media(media)
    media_player.play()

    #  wait so the media can be played for 1 second 
    #  irrespective for length of it.
    time.sleep(1)
    value = media_player.get_length()
    time.sleep(value/1000 +1)

    #  release PTT
    ser.dtr = False
    time.sleep(10)
