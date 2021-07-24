#include "uart.h"   
#include <stdlib.h>
#include <stdio.h>
//#include <time.h>


volatile char u8readUsart;
char testTransmiter[]= {"Hello world!\n"};



void respondUart(volatile char * request );
float generateTemp( void );
void tranferTemp( void );
void tranferHumid( void );


int main( void ){
	//srand(time(NULL)); Note: add this line then uart not work
	UART1_trasmit( testTransmiter );
	USART1_receive();
	u8readUsart= 0;
	while(1){
		if( u8readUsart != 0 ){
			respondUart(&u8readUsart);
			u8readUsart = 0;
		}			
	}
} 



void USART1_IRQHandler( void ){
	/* check error: parity, frame, noise, overun detect bit */
	if( (~(USART1->SR)&0x01u) && (~(USART1->SR>>1u)&0x01u) && (~(USART1->SR>>2u)&0x01u) && (~(USART1->SR>>3u)&0x01u) ){
		/* check interrupts flag and enable interrupts enable */
		if( ((USART1->SR>>5u)&0x01u) && ((USART1->CR1>>5u)&0x01u) ){
			u8readUsart = USART1->DR;
		}
	}
	/* reset all flag errors */
	USART1->DR;
}


void respondUart(volatile char * request ){
	switch( *request ){
		case 't':
			tranferTemp();
			break;
		case 'h':
			tranferHumid();
			break;
		default:
			UART1_trasmit("Defalut\n");
			break;
	}
}


float generateTemp( void ){
	float temp;
	temp= rand()%300;
	temp/=3;
	return temp;
}



//void handleTemp( float *inp, uint8_t *ng, uint8_t *tr, uint8_t *ch, uint8_t *dv ){
//    uint16_t temp;
//    temp= (*inp)*100;
//    *ng= temp/1000;
//    *tr= temp%1000/100;
//    *ch= temp%1000%100/10;
//    *dv= temp%1000%100%10;
//}





void tranferTemp( void ){
    float temp;
    char	buffer[6];
		uint16_t temp1;
    temp= generateTemp(); 
    //handleTemp(&temp, &ng, &tr, &ch, &dv);
		/* get 2 digits after . */
		temp1= temp*100;
		sprintf( buffer,"t%d", temp1);
    UART1_trasmit(buffer);
}

void tranferHumid( void ){
    float temp;
    char	buffer[6];
		uint16_t temp1;
    temp= generateTemp(); 
    //handleTemp(&temp, &ng, &tr, &ch, &dv);
		/* get 2 digits after . */
		temp1= temp*1000;
		sprintf( buffer,"h%d", temp1);
    UART1_trasmit(buffer);
}
