import spidev
import time


spi= spidev.SpiDev()
spi.open(0, 0) #use spi 0
spi.max_speed_hz= 1000000 # clk: 1MHz

def spiInit():
    # send and read data
    data= [ 0x0F, 0x00, 
            0x0C, 0x01,
            0x0B, 0x07,
            0x0A, 0x00,
            0x09, 0x00,]
    for i in range(0,5):
        spi.xfer(data[i:i+2])
    for i in range(1,9):
        data= [ i, 0]
        spi.xfer(data)
    
def dis( **kwargs ):
    row = kwargs["row"]
    value= kwargs["value"]
    #check value
    try:
        int( row )
        int(value)
        assert( 1<= row <=8)
        assert( 0<= value <= 255)
        # start spi
        data= [row, value]
        spi.xfer(data)
    except ValueError:
        print("ValueError\n")
    except AssertionError:
        print("AssertionError\n")
    

def main():
    try:
        spiInit()
        while True:
            for col in range(1,9):
                dis( row= col, value= 0xFF)
                time.sleep(0.05)
            for col in range(1,9):
                dis( row= col, value= 0)
                time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        spi.close()


main()
# read data
# nbyte= 2
# spi.readbytes(nbyte)