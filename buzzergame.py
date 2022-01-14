#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# configure both button and buzzer pins
up = 26
buzzer_pin = 18
left = 25

counter = 0

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# setup button pin asBu input and buzzer pin as output
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # check if button pressed
        if(GPIO.input(up) == 0):
            # set buzzer on
            counter+=1
            print(counter)
            GPIO.output(buzzer_pin, GPIO.HIGH)
        
        else:
            # it's not pressed, set button off
            GPIO.output(buzzer_pin, GPIO.LOW)
        

except KeyboardInterrupt:
    GPIO.cleanup()
    
