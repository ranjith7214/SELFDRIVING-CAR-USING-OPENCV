import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

print ("Distance Measurement In Progress")

gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.IN)


def distance():
    gpio.output(12,False)
    print ("Waiting For sensor to settle")
    time.sleep(0.1)

    gpio.output(12,True)
    time.sleep(0.00001)
    gpio.output(12,False)

    while gpio.input(16)==0:
        pulse_start = time.time()

    while gpio.input(16) == 1:
        pulse_end=time.time()

    pulse_duration=pulse_end - pulse_start

    dist = pulse_duration  * 17150

    dist= round(dist,2)
    return dist
    print("Distance:" ,dist, "cm")
print(distance())
gpio.cleanup()