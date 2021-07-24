import RPi.GPIO as GPIO
from time import sleep, time
import gpio

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
pwm= GPIO.PWM(16, 500) # pin 16 pwm with the freq 1Hz

i= int(0)

while 1:
    #blink led
    #gpio.blink(18)
    
    #blink led use PWM
    if (i==0):
     pwm.start(20)
     i+=1
     print("if statement")
   
    
    
    
    