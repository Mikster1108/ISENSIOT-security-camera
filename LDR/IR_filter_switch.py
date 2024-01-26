#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#pins to components
ldr_pin = 7
camera_pin = 37
threshold = 15000

#sets pin to camera as output pin
GPIO.setup(camera_pin, GPIO.OUT)


def rc_time (ldr_pin):
    count = 0
  
    #sets ldr pin to output and sets it to low to discharge the pin
    GPIO.setup(ldr_pin, GPIO.OUT)
    GPIO.output(ldr_pin, GPIO.LOW)
    time.sleep(0.1)

    #sets the pin back to input
    GPIO.setup(ldr_pin, GPIO.IN)
  
    #keeps counting until the pin goes high
    while (GPIO.input(ldr_pin) == GPIO.LOW):
        count += 1

    return count


def get_average(ldr_pin, measurements=10):
    total_count = 0

    for i in range(measurements):
        total_count += rc_time(ldr_pin)
        #adds a delay between measurements
        time.sleep(0.1)  

    average_count = total_count / measurements
    return average_count

#catch when script is interupted, cleanup correctly
try:
    #main loop
    while True:
        avg_value = get_average(ldr_pin, measurements=10)
         
        if avg_value > threshold: 
            #switches IR filter off 
            GPIO.output(camera_pin, GPIO.LOW)

        else:
            #switches IR filter on
            GPIO.output(camera_pin, GPIO.HIGH)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
