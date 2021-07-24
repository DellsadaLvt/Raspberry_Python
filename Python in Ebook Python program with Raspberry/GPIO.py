import RPi.GPIO as gpio
import time


gpio.setmode( gpio.BOARD )


# turn on or turn off
def controlLed( pin, value ):
    try:
        # chec the input value
        int(pin)
        int(value)
        assert(   0<= value <= 1 )
        # control gpio
        gpio.setup( pin , gpio.OUT )
        gpio.output( pin, value)
    except ValueError:
        print("Error ==> Enter the number\n")
    except AssertionError:
        print("Error ==> Check the magnitude of input\n")
        
        
# clean up 
def cleanup():
    gpio.cleanup()
    

# PWM   
# import RPi.GPIO as gpio

# gpio.setmode( gpio.BOARD )
# gpio.setup( 16, gpio.OUT )
# p= gpio.PWM( 16, 1000 )
# p.start(30)
     
# while True:
    # pass
    

# INPUT FUNCTION


    
    
    
    
    