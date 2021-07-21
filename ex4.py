import RPi.GPIO as GPIO
import time
import excercise3 as pwm

# INIT VALUE

btn0= 33
btn1= 35
btn2= 37
btnx= []
timeUseFncInp= int(0)
chooseLed= int(0)
duty= [0, 0, 0, 0]



# init config
GPIO.setmode(GPIO.BOARD)


#func0: handle button
# choose led
def handle_btn0( btn0 ):
    global chooseLed
    chooseLed += 1
    if( chooseLed > 2):
        chooseLed= 0
    pwm.controlPwmLed( led= chooseLed, duty= duty[chooseLed])
    print("Controling Led: {0}\n".format(chooseLed) )
    
# increasing duty pwm
def handle_btn1( btn1 ):
    global duty
    duty[chooseLed] += 10
    if (duty[chooseLed] > 100):
        duty[chooseLed]= 100
    pwm.controlPwmLed( led= chooseLed, duty= duty[chooseLed])
    print("The duty of Led {0}: {1}\n".format(chooseLed,duty[chooseLed]) )

#decreasing duty pwm
def handle_btn2( btn2 ):
    duty[chooseLed] -= 10
    if (duty[chooseLed] < 0):
        duty[chooseLed]= 0
    pwm.controlPwmLed( led= chooseLed, duty= duty[chooseLed])
    print("The duty of Led {0}: {1}\n".format(chooseLed,duty[chooseLed]) )
    
    
    
#func1
def initInput( **kwargs ):
    # get value
    temp= kwargs["btnx"]
    try:
        #check value
        int(temp)
        assert(0<= temp <= 40)
        # init object
        global btnx, timeUseFncInp
        btnx.append( temp )
        
        GPIO.setup( btnx[timeUseFncInp], GPIO.IN, pull_up_down= GPIO.PUD_DOWN )
        GPIO.add_event_detect( btnx[timeUseFncInp], GPIO.RISING, bouncetime= 100)
        if timeUseFncInp==0:
            GPIO.add_event_callback( btnx[timeUseFncInp], handle_btn0)
        elif timeUseFncInp==1:
            GPIO.add_event_callback( btnx[timeUseFncInp], handle_btn1)
        elif timeUseFncInp==2:
            GPIO.add_event_callback( btnx[timeUseFncInp], handle_btn2)
        #print(timeUseFncInp)
        timeUseFncInp += 1
    except ValueError:
        print("Value Erro\n")
        exit()
    except AssertionError:
        print("AssertionError\n")
        exit()




    




