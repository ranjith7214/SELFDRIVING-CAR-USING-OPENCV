import RPi.GPIO as GPIO
from time import sleep
#from sim800l import SIM800L
#sim800l=SIM800L('dev/serial0')
#sms="hi"
#destno="7092447008"
value=0
value2=0
value3=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(22,GPIO.OUT)


def gasleak():
    GPIO.setmode(GPIO.BCM)
    if(GPIO.input(23)):
        value2=GPIO.input(23)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)
        print(value2)
        print("alive")
            
    else:
        value2=GPIO.input(23)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        print(value2)
        print("leakage detected...!")
        sleep(3)
    if(GPIO.input(24)):
        value3=GPIO.input(24)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)
        print(value3)
        #print("alive")
            
    else:
        value3=GPIO.input(24)
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
        print(value3)
        print("leakage detected...!")
        sleep(5)
    #return value

# def gasleak1():
#     GPIO.setmode(GPIO.BCM)
#     if(GPIO.input(27)):
#         value2=GPIO.input(27)
#         GPIO.output(22,GPIO.LOW)
#         #print(value)
#         #print("alive")
#             
#     else:
#         value2=GPIO.input(27)
#         GPIO.output(22,GPIO.HIGH)
#         print(value2)
#         print("leakage detected...!")
#     return value2
# 
# def flame():
#     GPIO.setmode(GPIO.BCM)
#     if(GPIO.input(24)):
#         value3=GPIO.input(24)
#         GPIO.output(22,GPIO.LOW)
#         print(value3)
#         #print("alive")
#             
#     else:
#         value3=GPIO.input(24)
#         GPIO.output(22,GPIO.HIGH)
#         print(value3)
#         print("leakage detected...!")
#     return value3

#print(flame())
while True:
    gasleak()
#     gasleak1()
#     flame()
#             

        