import serial
import time


# keywords: t: request receive temperature
print("Start program")

ser = serial.Serial('/dev/ttyAMA0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
time.sleep(1)


def requestData( **kwargs ):
    command= kwargs["command"]
    print("send data" , command )
    ser.write(command)
    time.sleep(0.1)
    temp= ''
    humd= ''
    # read data
    if ser.inWaiting() > 0:
        temps= ser.read()
        if temps == "t":
            while ser.inWaiting() > 0:
                temp += ser.read()
            return temp
        elif temps == "h":
            while ser.inWaiting() > 0:
                humd += ser.read()
            return humd
    

def main():
    try:
        # ser.write('Hello World\r\n')
        # ser.write('Serial Communication Using Raspberry Pi\r\n')
        # ser.write('By: Embedded Laboratory\r\n')
        time1= time.time()
        time2= time.time()
        
        
        while True:
            if ( time.time() - time1 > 2):
                time1= time.time()
                # request read from stm by send data
                temperature= float(requestData(command= 't')) / 100
                print("Temperature is: ", temperature)
                humid= float(requestData(command= 'h')) / 100
                print("humid is: {0} \n".format(humid) )
                
            
                
                
    except KeyboardInterrupt:
        pass



    finally:
        ser.close()
        pass
        
        
main()        
        
        