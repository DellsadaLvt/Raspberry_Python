import RPi.GPIO as GPIO
import time


GPIO.setmode( GPIO.BOARD )

button= 37
time1= int(0)


#================= Normal func 
# try:
    # GPIO.setup(button, GPIO.IN, pull_up_down= GPIO.PUD_DOWN )
    # while True:
        # if( time.time() - time1 > 0.5):
            # time1= time.time()
            # print("The value is:", GPIO.input( button) )
# except KeyboardInterrupt:
    # pass

#================= Add dectect edge    
# try:
    # GPIO.setup(button, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
    # GPIO.add_event_detect( button, GPIO.RISING)
    # while True:
        # if( time.time() - time1 >= 1):
            # time1= time.time()
            # print(time1)
            # if GPIO.event_detected(button):
                # print("Button is pressed\n")
# except KeyboardInterrupt:
    # pass

# print("End the function")



#================= Threaded callacks
# def my_callback( button ):
    # print("The button is pressed\n")

# try:
    # GPIO.setup( button, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
    # GPIO.add_event_detect( button, GPIO.RISING, callback= my_callback)
    # while True:
        # if( time.time() - time1 > 1):
            # time1= time.time()
            # print("Hello Guy!\n")
# except KeyboardInterrupt:
    # pass

# print("End of the function\n")
button1= 35
button2= 37
def my_callback_one( button1 ):
    print("Button one is pressed\n")

def my_callback_two( button2 ):
    print("Button two is pressed\n")
    



try:
    GPIO.setup( button1, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
    GPIO.add_event_detect(button1, GPIO.RISING )
    GPIO.add_event_callback(button1, my_callback_one)
    GPIO.setup( button2, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
    GPIO.add_event_detect(button2, GPIO.RISING, bouncetime=1000) # when press button after 1000ms can dectect button pressed
    GPIO.add_event_callback(button2, my_callback_two)
    while True:
        pass
except KeyboardInterrupt:
    pass
    
print("End of the function\n")
    