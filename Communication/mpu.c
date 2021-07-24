/*======================= LIBRARIES =======================*/
#include<wiringPi.h>
#include<stdint.h>
#include<wiringPiI2C.h>
#include<stdio.h>
#include<math.h>


/*======================= DEFINE =======================*/
#define int_mpu 		16			// the pin int of mpu
#define Samp_rate		25			// 0x01: SMPLRT_DIV[7:0] is 1 ==> the sample rate: 500Hz
#define Config			26			// 0x02: FSYNC( input disable ), DLPF ( MODE 2)
#define Gyro_config 	27			// 0x08: no Self-test, full scale: 1 ==> +-500 do/sample
#define Acc_config		28			// 0x08: no self-test, full scale: 1 ==> +-4g, the sensity: 8192 LSB/g
#define Power_manager  	107			// 0x01: x axis gyroscope refer
#define Acc_x_out		59	
#define Acc_y_out		61
#define Acc_z_out		63
#define Int_config		55			// 0x80: int level is low active in data readly.
#define Ena_int 		56			// 0x01: set interrupts in only data readly mode

/*======================== VARIABLES ==================*/
int mpu;
volatile float pitchError;
/*======================= DECLARE FUNC =======================*/
void init_mpu(const int *mpu);
int16_t read_Acc(const int *mpu, uint8_t sensor_add);
float caculate_angle(const int *mpu, char mode[]);


/*======================= INTERRUPTS FUNCTION =======================*/
void handle_int_mpu( void ){
	float avg;
	avg= caculate_angle( &mpu, "pitch") ;//- pitchError ;
	printf("The pitch angle: %f\n", avg);
	/* avg= caculate_angle( &mpu, "roll");
	printf("The roll angle: %f\n", avg); */
}


/*======================= MAIN FUNCTION =======================*/
int main( void ){
	/* INITIAL SETUP IO WITH WIRINGPI LIB */
	wiringPiSetupPhys();
	
	/* INITIAL I2C */
	mpu = wiringPiI2CSetup(0x68);
	
	/* SETUP IO */
	pinMode( int_mpu, INPUT);
	
	/*INITIAL MPU*/
	init_mpu(&mpu);
	
	/* get the value mpu error */
	/* pitchError= 0;
	for( char i=0; i< 255; i++){
		pitchError+= caculate_angle( &mpu, "pitch");
	}
	pitchError/= 255;
	printf("pitch error: %f\n", pitchError); */
	
	/* CREATE INTERRUPTS */
	wiringPiISR( int_mpu, INT_EDGE_RISING, &handle_int_mpu);

	/*-------- WHILE LOOP ---------*/
	while(1){

	}
	return 0;
}

/*================ SUBROUTINE =====================*/
/*------------------------*/
void init_mpu(const int *mpu )
{
	wiringPiI2CWriteReg8(*mpu, Samp_rate, 199);
	wiringPiI2CWriteReg8(*mpu, Config, 2);
	wiringPiI2CWriteReg8(*mpu, Gyro_config, 0x10);
	wiringPiI2CWriteReg8(*mpu, Acc_config, 0x10);
	wiringPiI2CWriteReg8(*mpu, Int_config, 0);
	wiringPiI2CWriteReg8(*mpu, Ena_int, 1);
	wiringPiI2CWriteReg8(*mpu, Power_manager, 0x01);
	printf("\nComplete config mpu\n"); 
}

/*-----------------------*/
int16_t read_Acc( const int *mpu, uint8_t sensor_add){
			int16_t high	= wiringPiI2CReadReg8(*mpu, sensor_add);
			int16_t low		= wiringPiI2CReadReg8(*mpu, (sensor_add+1));
			int16_t	Acc 	= (high << 8) |low;
			printf("The high: %d\n",high);
			printf("The low : %d\n", low);
			printf("The Acc : %d\n\n", Acc);
			return 	Acc;	
}


float caculate_angle( const int *mpu, char mode[] ){
	printf("========================Get the value=======================\n");
	float ax = (float)read_Acc(&(*mpu), Acc_x_out)/4096.0;
	float ay = (float)read_Acc(&(*mpu), Acc_y_out)/4096.0;
	float az = (float)read_Acc(&(*mpu), Acc_z_out)/4096.0;
	
	printf("The ax: %f, ay: %f, az: %f\n", ax, ay, az);
	
	if( mode == "roll"){
		float roll= atan2(ay, sqrt(pow(ax,2) + pow(az,2)))*180/M_PI;
		//printf("\n************Roll X axial **************** \n");
		return roll;
	}
	else if( mode == "pitch"){
		float pitch= atan2(ax, sqrt(pow(az,2) + pow(ay,2)))*180/M_PI;
		//printf("\n************Pitch Y axial **************** \n");
		return pitch;
	}
	else
		printf("\nThe value invalid\n");
}





