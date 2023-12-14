#include <stdio.h>

#include <pigpio.h>

#define GPIO_PIN 26

int main()
{
   if (gpioInitialise()<0) return 1;

	gpioSetMode(GPIO_PIN, PI_OUTPUT);
        gpioWrite(GPIO_PIN,1); // 1/HIGH turns filter on (day view) 0/LOW turns filter off (night view)
        
        gpioTerminate();
        
        return 0;
      }
