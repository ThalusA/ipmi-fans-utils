#!/usr/bin/env python3

from sys import argv, exit, stdout
from os  import popen, environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time

command = "ipmitool -U root -P calvin -H 172.30.42.220 raw 0x30 0x30 0x02 0xff %s"
last_value = 299

pygame.joystick.init()
pygame.display.init()

joystick = pygame.joystick.Joystick(0)
seconds = time.time()

joystick.init()

def update(value, l_value):
    if (abs(value - l_value) > 2):
        print(f"New fan speed: {value}%   ", end='\r')
        popen(command % hex(value))
        return value
    return l_value 


while 1:
    pygame.event.pump() 
    val = joystick.get_axis(2)
    if (val > 0.9999): val = 1
    val = 100 - int((val + 1) * 50)
    current_time = time.time()
    if (current_time - seconds > 0.1): 
        last_value = update(val, last_value)
        seconds = current_time

