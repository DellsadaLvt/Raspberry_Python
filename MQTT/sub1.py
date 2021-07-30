"""
 * Call loop() frequently to maintain network traffic flow with the broker
    * Or use loop_start() to set a thread running to call loop() for you.
    * Or use loop_forever() to handle calling loop() for you in a blocking
    * function.

Reference:
    def publish(self, topic, payload=None, qos=0, retain=False, properties=None):
    def connect(self, host, port=1883, keepalive=60, bind_address="", bind_port=0,
                clean_start=MQTT_CLEAN_START_FIRST_ONLY, properties=None):
                
    class Client:
         def __init__(self, client_id="", clean_session=None, userdata=None,
                 protocol=MQTTv311, transport="tcp"):
                 
    def subscribe(self, topic, qos=0, options=None, properties=None):       

    def loop(self, timeout=1.0, max_packets=1):
    def loop_start(self):
    def loop_forever(self, timeout=1.0, max_packets=1, retry_first_connection=False):
"""

import paho.mqtt.client as mqtt
import time

tempLv= tKc= 0
tempKc= tLv= 0

isConnected= False
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    if ( str(rc) == '0'):
        global isConnected
        isConnected= True
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # def subscribe(self, topic, qos=0, options=None, properties=None):
    #client.subscribe([ ("Livingroom/Temperature", qos= 1), ("Kitchen/Temperature", qos= 1)])
    #client.subscribe("Kitchen/Temperature", qos= 1)
    client.subscribe([("Livingroom/Temperature", 1), ("Kitchen/Temperature", 1)])
 

 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" " + str(msg.payload))
    #print("message id:  ", msg.mid)
    if msg.topic == "Livingroom/Temperature":
        global tempLv
        tempLv= float(bytes.decode(msg.payload))
    elif msg.topic == "Kitchen/Temperature":
        global tempKc
        tempKc= float(bytes.decode(msg.payload))
        
 


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
 
# information
user= "admin"
passwd= "123456"
clientID= "pii"


# Create an MQTT client and attach our routines to it.
#def __init__(self, client_id="", clean_session=None, userdata=None,
                 #protocol=MQTTv311, transport="tcp"):
client = mqtt.Client( client_id= clientID, clean_session= False)
client.username_pw_set( username= user, password= passwd)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.reconnect_delay_set(min_delay= 1, max_delay= 60)
#def connect(self, host, port=1883, keepalive=60, bind_address="", bind_port=0,
                #clean_start=MQTT_CLEAN_START_FIRST_ONLY, properties=None):
#client.connect("broker.emqx.io", 1883, 60)
client.connect( host= "192.168.1.2", port= 1883, keepalive= 60)
client.loop_start()
#wait for connected
while isConnected != True:
    time.sleep(0.2)
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
#client.loop_forever()
# start loop in another thread


def handleTemp():
    global tempLv, tKc, tLv
    if tempKc > 90 and tempKc < 100:
        if tempKc != tKc:
            tKc= tempKc
            print("KitChen overload: {0:.5}=====================>".format(tKc))
    if tempLv > 90 and tempLv < 100:
        if tempLv != tLv:
            tLv= tempLv
            print("Turn on the air conditioner: {0:.5}============>".format(tLv))
    if tempLv == 200:
        print("Pulisher is not connect=====================================================>")
        tempLv= 201


        

def main():
    try:
        tim= time.time()
        while True:
            if( time.time() - tim > 0.1):
                handleTemp()
                tim= time.time()
    except KeyboardInterrupt:
        exit()
        
    finally:
        client.loop_stop()
        client.disconnect()
        
main()
    
    
    
    