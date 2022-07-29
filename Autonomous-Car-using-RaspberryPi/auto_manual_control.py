import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from sensor import distance



def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7,gpio.OUT)
    gpio.setup(11,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.OUT)

def turn_left(tf):


    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()

def forward(tf):
    
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
   
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()




def key_input(event):
    init()
    print 'Key:' , event.char
    key_press=event.char
    sleep_time=0.040
    

    if key_press.lower() == 'w':
        forward(2)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    else:
        pass

    curDis = distance('cm')
    print('curDis is', curDis)

    if curDis < 20:
        init()
        reverse(2)
    

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()


