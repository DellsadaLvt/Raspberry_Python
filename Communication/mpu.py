# sudo i2cdetect -y 1 ==>0x68
import RPi.GPIO as GPIO
import smbus
import time
import math
from ctypes import *



libCalC= CDLL("./generateAx.so")
bus= smbus.SMBus(1)
addrMpu= 0x68


                        
bus.write_byte_data(addrMpu, 25, 199)  
bus.write_byte_data(addrMpu, 26, 2)  
bus.write_byte_data(addrMpu, 27, 0x10)  
bus.write_byte_data(addrMpu, 28, 0x10)  
bus.write_byte_data(addrMpu, 107, 1)  

Acc_rawX= ' '

#add one line

while True:
  axh= bus.read_byte_data( addrMpu, 59 )
  axl= bus.read_byte_data( addrMpu, 60 )
  Acc_rawX=str(libCalC.generateAx(axh, axl))
  print(Acc_rawX)
  print(type(Acc_rawX))
  exit()    
  # ayh= bus.read_byte_data( addrMpu, 61 )
  # ayl= bus.read_byte_data( addrMpu, 62 )
  # Acc_rawY= libCalC.generateAx(ayh, ayl)
  # azh= bus.read_byte_data( addrMpu, 63 )
  # azl= bus.read_byte_data( addrMpu, 64 )
  # Acc_rawZ= libCalC.generateAx(azh, azl)
  # Acc_angle_y = (math.atan(Acc_rawX)/math.sqrt(pow((Acc_rawY),2) + pow((Acc_rawZ),2))*180/3.14)
  # print("The raw value")
  # print(Acc_rawX)
  # print(Acc_rawY)
  # print(Acc_rawZ)
  # print("The acc:" ,Acc_angle_y)
  # time.sleep(0.5)




