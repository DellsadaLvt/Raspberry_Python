import RPi.GPIO as GPIO
import time


# INIT CONFIG
GPIO.setmode(GPIO.BOARD)
LED= 12
LED2=16
LED3=18
GPIO.setup( LED, GPIO.OUT)
GPIO.setup( LED2, GPIO.OUT)
GPIO.setup( LED3, GPIO.OUT)

pwm= GPIO.PWM( LED, 1000)
pwm2= GPIO.PWM( LED2, 1000)
pwm3= GPIO.PWM( LED3, 1000)

pwm.start(0)
pwm2.start(0)
pwm3.start(0)

def pwmLed( pwmx ):
    for i in range(0, 101, 10 ):
        #print(i)
        pwmx.ChangeDutyCycle(i)
        time.sleep(0.1)
    for i in range(90, -1, -10 ):
        #print(i)
        pwmx.ChangeDutyCycle(i)
        time.sleep(0.1)


try:
    while True:
        pwmLed( pwm )
        pwmLed( pwm2 )
        pwmLed( pwm3 )
            

except KeyboardInterrupt:
    pass
    
pwm.stop()
GPIO.cleanup()


