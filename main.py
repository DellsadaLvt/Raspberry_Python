import excercise3 as fnc3
import ex4        as fnc4

# INIT VALUE
led= (12,16,18)
btn0= 33
btn1= 35
btn2= 37


def ex3():
    try:
        fnc3.initPwm( ledPin= LED,  freq=800, startDuty=0)
        fnc3.initPwm( ledPin= LED2, freq=800, startDuty=0)
        fnc3.initPwm( ledPin= LED3, freq=800, startDuty=0)
        while True:
            fnc3.pwm3Led()
    except KeyboardInterrupt:
        pass 
    fnc3.cleanGPIO()




def ex4():
    try:
        fnc3.initPwm( ledPin= led[0], freq=800, startDuty = 0)
        fnc3.initPwm( ledPin= led[1], freq=800, startDuty = 0)
        fnc3.initPwm( ledPin= led[2], freq=800, startDuty = 0)
        
        fnc4.initInput( btnx= btn0 )
        fnc4.initInput( btnx= btn1 )
        fnc4.initInput( btnx= btn2 )
        while True:
            pass
            
    except KeyboardInterrupt:
        pass
    fnc3.cleanGPIO()    
        
        
def main():
    ex4()
    
    
main()