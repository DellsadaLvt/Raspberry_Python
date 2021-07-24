#include <stdio.h>
#include <stdint.h>
#include <wiringPi.h>
#include <assert.h>

void checkconnect( int inp ){
	printf("The input is: %d\n", inp);
}

void pwm( uint8_t value ){
	/* check the value */
	assert( (value >= 0 && value <= 100));
	/* config gpio */
	wiringPiSetupPhys();
	pinMode( 12, PWM_OUTPUT);
	pwmSetMode(PWM_MODE_BAL);
	pwmSetRange(1024);
	pwmSetClock(1);
	/* convert value */
	uint16_t duty;
	duty= 1024 - 1024/100*(100-value);
	//printf("the duty is: %d\n", duty);
	/* write pwm */
	pwmWrite( 12, duty);
}