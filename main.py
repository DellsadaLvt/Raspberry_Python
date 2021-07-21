# <<<<<<< HEAD
# # this code in ex1
# =======
# # code in ex4
# >>>>>>> ex4
import excercise3 as fnc3
# this code in master

# INIT VALUE
LED= 12
LED2=16
LED3=18

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


def main():
    ex3()
    
    
main()