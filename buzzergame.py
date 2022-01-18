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
GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_UP)

isDown = False
isDown2 = False
t =5

try:
    while True:
        # check if button pressed
        if(GPIO.input(up) == 0):
            isDown = False

        if(GPIO.input(up) == 1) and isDown == False:
            isDown = True
            counter+=1
            print(counter)

        
        
        #button 2
        if(GPIO.input(left) == 0):
            isDown2 = False
       
        if(GPIO.input(left) == 1) and isDown2 == False:
            isDown2 = True
            counter-=1
            print(counter)
            
        if counter == -50:
            print("Player Left Wins!")
        if counter == 50:
            print("Player Up Wins!")
except KeyboardInterrupt:
    GPIO.cleanup()
    
