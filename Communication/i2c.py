# sudo i2cdetect -y 1 ==>0x68
import RPi.GPIO as GPIO
import smbus
import time
import math
from ctypes import *

libCalC= CDLL("./generateAx.so")

# config gpio
intPin= 16
btnx= []
timeUseFncInp= int(0)
GPIO.setmode( GPIO.BOARD )


# use i2c1: pin 3: sda, pin 5: scl
bus= smbus.SMBus(1)
addrMpu= 0x68


# add of register mpu
sampleRate= 25
config    = 26
gyroConfig= 27
accConfig = 28
activeInt = 55
enableInt = 56
pwrManage = 107
accX      = 59
accY      = 61
accZ      = 63


def handle_intMpu( intPin ):
    pitch= caculateAngle( mode= "pitch")
    roll= caculateAngle( mode="roll")
    print("The pitch angle: {0}".format(pitch))
    print("The roll angle: {0}".format(roll))

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
            GPIO.add_event_callback( btnx[timeUseFncInp], handle_intMpu)
        
        #print(timeUseFncInp)
        timeUseFncInp += 1
    except ValueError:
        print("Value Erro\n")
        exit()
    except AssertionError:
        print("AssertionError\n")
        exit()


def configMpu():
    bus.write_byte_data(addrMpu,pwrManage, 0)
    bus.write_byte_data(addrMpu, sampleRate, 99)
    bus.write_byte_data(addrMpu,config, 5)
    bus.write_byte_data(addrMpu,gyroConfig, 0x10)
    bus.write_byte_data(addrMpu,accConfig, 0x10)
    bus.write_byte_data(addrMpu,enableInt, 1)
    bus.write_byte_data(addrMpu,activeInt, 0x80)
    bus.write_byte_data(addrMpu,pwrManage, 1)


def readAcc( **kwargs ):
    addr= kwargs["addr"]
    # Acch = bus.read_byte_data(addrMpu, addr)
    # Accl = bus.read_byte_data(addrMpu, addr + 1)
    # Acc  = ( Acch << 8 ) | Accl
    return (bus.read_byte_data(addrMpu, addr)<<8) | bus.read_byte_data(addrMpu, addr + 1)

def caculateAngle(**kwargs):
    mode= kwargs["mode"]
    Accx= readAcc( addr= accX)/4096.0
    Accy= readAcc( addr= accY )/4096.0
    Accz= readAcc( addr= accZ )/4096.0
    if mode=="pitch":
        pitch= math.atan2(Accx,math.sqrt(math.pow(Accy,2) + math.pow(Accz, 2)))*180/math.pi
        return pitch
    
    elif mode== "roll":
        roll= math.atan2(Accy,math.sqrt(math.pow(Accx,2) + math.pow(Accz, 2)))*180/math.pi
        return roll

def main():
    try:
        initInput( btnx= intPin )
        configMpu()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    
    finally:
        bus.close()
        
main()       
        

            