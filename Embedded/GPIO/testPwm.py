import time
import RPi.GPIO as GPIO
from ctypes import *
libCalc= CDLL("./libPwM.so")



# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(12, GPIO.OUT)

# p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
# p.start(0)


libCalc.controlLed( int(50))




