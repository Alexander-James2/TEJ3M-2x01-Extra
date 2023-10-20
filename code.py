# Created by Alex James
# Created on Oct. 2023
# Template taken from Adafruit site

#This program Blinks the built in LED on the Pi Pico

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
