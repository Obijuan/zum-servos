#!/usr/bin/python
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
#-- bq human right to technology
#-- bq Tienes derecho a la tecnologia
#-----------------------------------------------------------------
#-- Servo class
#-- (c) Juan Gonzalez-Gomez (obijuan).  May-2013
#-----------------------------------------------------------------
#-- Controlling the position of servos from the PC
#-- The board driving the servos (zum bt-328, arduino, skymega...)
#-- should have the firmware zum-servos 
#-----------------------------------------------------------------

import time

class IncorrectAngle():
  pass


class Servo(object):
  """Servo class. For accessing to all the Servos"""
  
  def __init__(self, sp, dir = 0):
    """Arguments: serial port and servo number"""
    self.sp = sp     #-- Serial device
    self.dir = dir   #-- Servo number
    self._pos = 0;   #-- Current pos

  def __str__(self):
    str1 = "Servo: {0}\n".format(self.dir)
    str2 = "Serial port: {0}".format(self.sp.name)
    return str1 + str2
  
  def set_pos(self, pos):
    """Set the angular servo pos. The pos is an integer number
       in the range [-90 ,90] """
    
    #-- Check that the pos in the range [-90,90] 
    if not (-90 <= pos <= 90): 
      raise IncorrectAngle()
      return
    
    #-- Convert the pos to an integer value
    pos = int(round(pos))
      
    #-- Build the frame   
    frame = self.dir + str(pos) + "\r"
    
    #-- Debug
    #print (frame)
    
    #-- Send the frame
    self.sp.write(frame)
    
    #-- Store the current servo pos
    self._pos = pos
    
  @property
  def pos(self):
    """Read the current servo pos"""
    return self._pos

  @pos.setter
  def pos(self, value):
    """Set the sero pos"""
    self.set_pos(value)


    
