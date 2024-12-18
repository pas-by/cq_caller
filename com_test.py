#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  file name : com_test.py
#  description : This file is used to test the serial communication between the computer and the arduino.
#  author : Yoonseok Lee
#  date : 2019. 8. 20.

import serial
import time

ser = serial.Serial('COM10', 9600)

while True:
    # GRD is pin 5
    # DTR is pin 4
    ser.dtr = True
    time.sleep(5)
    ser.dtr = False
    time.sleep(5)
