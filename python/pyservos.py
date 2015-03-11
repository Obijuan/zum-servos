#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#-----------------------------------------------------------------------
# (C)2015 Juan Gonzalez (Obijuan)
# Released under the GPL license
#-----------------------------------------------------------------------
#-- Client for the Zum Servo server
#-- Create scripts for moving the servos easily
#-----------------------------------------------------------------------

import time
import serial
import Servo

#-- Change the serial port here
SERIAL_PORT = "/dev/ttyUSB0"

#-- short version (not interactive)
with serial.Serial(SERIAL_PORT, 19200) as sp:
    a = Servo.Servo(sp, dir = 'a')
    b = Servo.Servo(sp, dir = 'b')
    
    #-- Init servos
    a.pos = 0
    b.pos = 0
    time.sleep(1)
    
    #-- Initial pos
    a.pos = 80
    b.pos = -80
    time.sleep(1)
    
    #-- Simple sequence
    for i in range(10):
      a.pos = -a.pos
      b.pos = -b.pos
      time.sleep(1)
    

