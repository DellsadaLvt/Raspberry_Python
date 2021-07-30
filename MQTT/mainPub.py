"""
Reference:
    def publish(self, topic, payload=None, qos=0, retain=False, properties=None):
    def connect(self, host, port=1883, keepalive=60, bind_address="", bind_port=0,
                clean_start=MQTT_CLEAN_START_FIRST_ONLY, properties=None):
                
    class Client:
         def __init__(self, client_id="", clean_session=None, userdata=None,
                 protocol=MQTTv311, transport="tcp")
    
    reconnect_delay_set(min_delay=1, max_delay=120)
"""

import paho.mqtt.client as mqttclient
import time
import random


def on_connect(client, userdata, flags, rc, properties=None):
        print("Connection returned " + str(rc))
        if rc==0:
            print("Connected")
            global connected
            connected= True
        else:
            print("Connect error")

# information connection
connected= False
brokerAddr= "192.168.1.2"
port= 1883
user= "admin"
passwd= "123456"
clientID= "pi"

# connect to broker
#def __init__(self, client_id="", clean_session=None, userdata=None,
              #protocol=MQTTv311, transport="tcp"):
client= mqttclient.Client(client_id="pi", clean_session= True)
client.username_pw_set(username= user, password=passwd)
client.reconnect_delay_set(min_delay= 1, max_delay= 60)
#client.client_id= clientID
client.on_connect= on_connect

#test
client.will_set("Livingroom/Temperature", payload= 200, qos=1, retain=True)
client.connect(host= brokerAddr, port= port, keepalive= 30)
client.loop_start()
while connected != True:
    time.sleep(0.2)
 


def main():
    try:
        tim= time.time()
        while True:
            if ( time.time() - tim > 1 ):
                temp= random.random()*100
                #def publish(self, topic, payload=None, qos=0, retain=False, properties=None):
                client.publish("Livingroom/Temperature","{0:.3}".format(temp),qos=1, retain= True)
                temp= random.random()*100
                client.publish("Kitchen/Temperature", "{0:.3}".format(temp), qos=1, retain= True)
                #client.loop_stop()
                tim= time.time()     
    except KeyboardInterrupt:
        exit() 
    finally:
        client.loop_stop()
        client.disconnect()
            
            
main()            