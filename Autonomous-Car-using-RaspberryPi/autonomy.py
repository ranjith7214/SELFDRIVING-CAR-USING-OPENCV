import RPi.GPIO as gpio
import time
import sys
#import Tkinter as tk
from  distance import distance
import random



def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(7,gpio.OUT)
    gpio.setup(8,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(26,gpio.OUT)

def turn_left(tf):


    gpio.output(7,False)
    gpio.output(8,True)
    gpio.output(13,True)
    gpio.output(26,False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    
    gpio.output(7,True)
    gpio.output(8,False)
    gpio.output(13,False)
    gpio.output(26,True)
    time.sleep(tf)
    gpio.cleanup()

def forward(tf):
    
    gpio.output(7,True)
    gpio.output(8,False)
    gpio.output(13,True)
    gpio.output(26,False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
   
    gpio.output(7,False)
    gpio.output(8,True)
    gpio.output(13,False)
    gpio.output(26,True)
    time.sleep(tf)
    gpio.cleanup()


def check_front():
    init()
    dist =distance()
    if dist> 40:
        init()
        forward(tf)
    if dist<40:
        print('Too close,need to move back!!',dist)
        init()
        reverse(2)
        init()
        turn_right(2)
        dist=distance()
        if dist < 40:
            print('Too Close,Reassessing Path' , dist)
            init()
            turn_left(2)
            init()
            reverse(2)
            dist =distance()
            if dist < 30:
                print('Too Close, giving up', dist)
                sys.exit()
tf=0.030
while True:
    init()
    forward(tf)
    check_front()
# def autonomy():
#     tf=1
#     x=random.randrange(0,4)
# 
#     if x == 0:
#         for y in range(30):
#             check_front()
#             print("first")
#             init()
#             forward(tf)
#     elif x == 1:
#         for y in range(30):
#             check_front()
#             init()
#             forward(tf)
#     elif x == 2:
#         for y in range(30):
#             check_front()
#             init()
#             turn_right(tf)
#     elif x == 3:
#         for y in range(30):
#             check_front()
#             init()
#             turn_left(tf)
# 
# for z in range(10):
#     autonomy()

       
                       
