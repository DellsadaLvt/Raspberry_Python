import RPi.GPIO as GPIO
from time import sleep


def blink( pin ):
    GPIO.output(pin, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin, GPIO.LOW)
    sleep(1)
        
       
