#gcc -shared -o generateAx.so -fPIC generateAx.c


from ctypes import *
import RPi.GPIO as GPIO
import time

# CONFIG
libCalc= CDLL("./libc.so")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

# INIT VALUES
t1= 0
t2= 0

while 1:
    if (time.time() - t1 >=2 ):
        t1= time.time()
        print("The t1", t1)
        libCalc.checkconnect(20)
        libCalc.pwm(10)
        
    elif ( time.time() - t2 >=4  ):
        t2= time.time()
        print("the t2",t2)
        # p = GPIO.PWM(18, 50)  # channel=12 frequency=50Hz
        # p.start(10)
	libCalc.pwm(80)
    


