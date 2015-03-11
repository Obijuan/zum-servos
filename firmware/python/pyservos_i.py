#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#-----------------------------------------------------------------------
# (C)2015 Juan Gonzalez (Obijuan)
# Released under the GPL license
#-----------------------------------------------------------------------
#-- Interactive version
#--
#-- Open it with  ipython pyservos_i.py -i
#-- Then you directly can access the servos from the ipython console:
#--  Ej.
#--        a.pos = 80   -->  Move servo a to 80 degrees
#--        b.pos = -50  -->  Mover servo c to -50 degrees

import serial
import Servo

#-- Change the serial port here
SERIAL_PORT = "/dev/ttyUSB0"

def serial_port(sname = "/dev/ttyUSB0"):
	"""Open the serial port"""
	try:
		sp = serial.Serial(sname, 19200)
		return sp
	except serial.SerialException:
		sys.stderr.write("Error opening the port {0}".format(sname))
		sys.exit(1)

#-------- Interactive version

#-- Open serial port
sp = serial_port(SERIAL_PORT)

#-- Define the servos
a = Servo.Servo(sp, dir = 'a')
b = Servo.Servo(sp, dir = 'b')
c = Servo.Servo(sp, dir = 'c')
d = Servo.Servo(sp, dir = 'd')

#-- Init servos
for s in [a, b, c, d]:
	s.pos = 0


