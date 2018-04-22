import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while(1):
    result = GPIO.input(27)
    if result == 1:
        print('1')
        time.sleep(0.05)
    else:
        print('0')
        time.sleep(0.05)
