/* 
* gcc Subcribe.c -o sub  -lpaho-mqtt3c $(mariadb_config --libs) $(mariadb_config --cflags)
*/
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
/* #include <mysql.h> */
#include "MQTTClient.h"

/* Config mysql */
/*     MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    char *server = "localhost";
    char *user = "admin_10";
    char *password = "123456"; 
    char *database = "MQTT"; */
/*******************************/

/**************************************
		Access Information
	Broker: broker.emqx.io
	TCP Port: 1883
	Websocket Port: 8083
	TCP/TLS Port: 8883
	Websocket(ws)/TLS Port: 8084
*****************************************/

#define ADDRESS   		"tcp://broker.emqx.io:1883"
#define CLIENTID		"YoSub"
#define SUB_TOPIC 		"test/topic"
#define QOS   		 		1

void publish(MQTTClient client, char* topic, char* payload); 
int on_message( void *context, char *topicName, int topicLen, MQTTClient_message *message );


int main ( void ){
	/* CONFIG MQTT */
	MQTTClient client;
	MQTTClient_create(&client, ADDRESS, CLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
	MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
	// conn_opts.username = "your_username";
	// conn_opts.password = "your_password";
	MQTTClient_setCallbacks(client, NULL, NULL, on_message, NULL);
	/*************************************************************************************/
	
	/* CHECK STATUS MQTT */
	int rc;
	if( (rc= MQTTClient_connect(client, &conn_opts)) != MQTTCLIENT_SUCCESS ){
		printf("Failed to connect, return code %d\n, rc");
		exit(-1);
	}
	
	// listen for operation
	MQTTClient_subscribe(client, SUB_TOPIC, 0);
	
	while(1){
		//publish(client, PUB_TOPIC, "hello world!");
		//sleep(3);
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
	pubmsg.retained = 0;
	MQTTClient_deliveryToken token;
	MQTTClient_publishMessage(client, topic, &pubmsg, &token);
	MQTTClient_waitForCompletion(client, token, 1000L);
	printf("Message '%s' with delivery token %d deliveried\n", payload, token);
}

int on_message( void *context, char *topicName, int topicLen, MQTTClient_message *message ){
	char* payload = message->payload;
	printf("Received message: %s\n", payload);
	/* working with database */
	// ket noi database
	/* conn = mysql_init(NULL);
	if( mysql_real_connect( conn, server, user, password, database, 0, NULL, 0 	) == NULL	){
		fprintf(stderr, "%s\n", mysql_error(conn));
		mysql_close( conn );
		exit(1);
	}  */
	/* init sql */
	/* char sql[200];
	// insert data to database
	sprintf(sql, "insert into demoMQTT (data) values (%s)", payload);
	mysql_query(conn, sql); */
	/* Check capacity */
	/* sprintf(sql, "select max(STT) from demoMQTT");
	mysql_query(conn,sql);
	res = mysql_store_result(conn); 	
	row = mysql_fetch_row(res);
	//printf("%s\n", row[0]);
	if( atoi(row[0]) > 60){
		sprintf(sql, "delete from demoMQTT where STT < 62");
		mysql_query(conn,sql);
		sprintf(sql, "alter table demoMQTT auto_increment = 1");
		mysql_query(conn,sql);
	}  */
	// disconnect database
	/* mysql_close(conn); */
	/**************************/
	MQTTClient_freeMessage(&message);
	MQTTClient_free(topicName);
	return 1;
}

