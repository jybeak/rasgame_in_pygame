import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)
button01 = True
while(1):
    if (GPIO.input(17) == 1) and (button01 == True):
        print(True)
        button01 =  False
    elif (GPIO.input(17)) == 0 and  (button01 == False):
        print(False)
        button01 =  True