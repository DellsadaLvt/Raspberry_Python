# code in ex4
import excercise3 as fnc3


# INIT VALUE
LED= 12
LED2=16
LED3=18
# code in ex4
def ex3():
    try:
        fnc3.initPwm( ledPin= LED,  freq=800, startDuty=0)
        fnc3.initPwm( ledPin= LED2, freq=800, startDuty=0)
        fnc3.initPwm( ledPin= LED3, freq=800, startDuty=0)
        while True:
            fnc3.pwm3Led()
    except KeyboardInterrupt:
        pass 
    fnc3.endOfPwm()

# code in ex4
# code in ex4
# code in ex4
def main():
    ex3()
    
    
main()