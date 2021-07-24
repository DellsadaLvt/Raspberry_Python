from gpiozero import LED
from time     import sleep


led= LED(24)

class GPIO:
    def blink( self ):
        led.on()
        sleep(1)
        led.off()
        sleep(1)
        

     