import paho.mqtt.client as paho
import time


broker= "ws4"
port= 8883
conn_flag= False

def on_connect(client, userdata, flags, rc):
    global conn_flag
    conn_flag= True
    print("connected", conn_flag)
    conn_flag= True
    
def on_log( client, userdata, level, buf):
    print("buffer", buf)
    
 
def on_disconnect( client, userdata, rc):
    print("client disconnected ok")
    
client1= paho.Client("control1")
client1.on_log= on_log
client1.tls_set('/etc/mosquitto/ca_certificates/ca.crt')
client1.on_connect= on_connect
client1.on_disconnect= on_disconnect
client1.connect( broker, port)

while conn_flag != True:
    time.sleep(1)
    print("...")
    client1.loop()
    
time.sleep(3)
print("publish")
client.publish("house/bulb", "hi there")
time.sleep(2)
client1.loop()
time.sleep(2)
client1.disconnected()