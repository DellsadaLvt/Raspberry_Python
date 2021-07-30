#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include "MQTTClient.h"


/**************************************
		Access Information
	Broker: broker.emqx.io
	TCP Port: 1883
	Websocket Port: 8083
	TCP/TLS Port: 8883
	Websocket(ws)/TLS Port: 8084
*****************************************/

#define ADDRESS   		"tcp://broker.emqx.io:1883"
#define CLIENTID		"YourClientID"
//#define SUB_TOPIC 		"test/topic1"
#define PUB_TOPIC		"test/topic"
#define QOS   		 		1

void publish(MQTTClient client, char* topic, char* payload); 
int on_message( void *context, char *topicName, int topicLen, MQTTClient_message *message );

int main ( void ){
	MQTTClient client;
	MQTTClient_create(&client, ADDRESS, CLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
	MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
	// conn_opts.username = "your_username";
	// conn_opts.password = "your_password";
	MQTTClient_setCallbacks(client, NULL, NULL, on_message, NULL);
	
	int rc;
	if( (rc= MQTTClient_connect(client, &conn_opts)) != MQTTCLIENT_SUCCESS ){
		printf("Failed to connect, return code %d\n, rc");
		exit(-1);
	}
	
	// listen for operation
	//MQTTClient_subcribe(client, SUB_TOPIC, 0);
	int i= 0;
	while(1){
		char msg[200];
		sprintf(msg, "%d", i );
		publish(client, PUB_TOPIC, msg);
		i++;
		sleep(1);
	}
	MQTTClient_disconnect(client, 1000);
	MQTTClient_destroy(&client);
	return rc;
}


void publish(MQTTClient client, char* topic, char* payload){
	MQTTClient_message pubmsg = MQTTClient_message_initializer;
	pubmsg.payload = payload;
	pubmsg.payloadlen = strlen(pubmsg.payload);
	pubmsg.qos = 1;
	pubmsg.retained = 0; // if retained= 1 ==>
	MQTTClient_deliveryToken token;
	MQTTClient_publishMessage(client, topic, &pubmsg, &token);
	MQTTClient_waitForCompletion(client, token, 1000L);
	printf("Message '%s' with delivery token %d deliveried\n", payload, token);
}

int on_message( void *context, char *topicName, int topicLen, MQTTClient_message *message ){
	char* payload = message->payload;
	printf("Received message: %s\n", payload);
	MQTTClient_freeMessage(&message);
	MQTTClient_free(topicName);
	return 1;
}
