import RPi.GPIO as GPIO
import time


# INIT CONFIG
GPIO.setmode(GPIO.BOARD)

# # INIT VALUE
# LED= 12
# LED2=16
# LED3=18
timeUseFucInitPwm= int(0)
pwm= []


# func 0
def initPwm( **kwargs ):
    # init input
    ledPin= kwargs["ledPin"]
    freq  = kwargs["freq"]
    startDuty  = kwargs["startDuty"]
    
    #check paremeter
    try:
        int(ledPin)
        int(freq)
        int(startDuty)
        assert( 0 <= ledPin <= 40 )
        assert( 0 <= freq <= 1000 )
        assert( 0 <= startDuty <= 100 )
    except ValueError:
        print("Input must be a number\n")
        exit()
    except AssertionError:
        print("Check assert of values\n")
        exit()
    
    # start setup pwm
    global pwm
    global timeUseFucInitPwm
    GPIO.setup( ledPin, GPIO.OUT )
    pwm.append( GPIO.PWM( ledPin, freq ))
    #print("type of pwm",type(pwm))
    pwm[timeUseFucInitPwm].start(startDuty)
    timeUseFucInitPwm += 1

# function 1
def pwmLed( pwmx ):
    for i in range(0, 101, 10 ):
        #print(i)
        pwmx.ChangeDutyCycle(i)
        time.sleep(0.1)
    for i in range(90, -1, -10 ):
        #print(i)
        pwmx.ChangeDutyCycle(i)
        time.sleep(0.1)


def pwm3Led():
    pwmLed( pwm[0] )
    pwmLed( pwm[1] )
    pwmLed( pwm[2] )
    
    
def endOfPwm():   
    pwm[0].stop()
    pwm[1].stop()
    pwm[2].stop()
    GPIO.cleanup()


