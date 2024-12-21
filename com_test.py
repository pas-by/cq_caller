#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  file name : com_test.py
#  description : This file is used to test the serial communication between the computer and the radio.
#  author : Yoonseok Lee
#  date : 2019. 8. 20.

import serial
import time

#  get comport object
ser = serial.Serial('COM10', 9600)

while True:
    # GRD is pin 5
    # DTR is pin 4
    ser.dtr = True
    print("ON")
    print()
    time.sleep(5)

    ser.dtr = False
    print("OFF")
    print()
    time.sleep(5)
