import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
a = 0
while  a<30:
    GPIO.output(17, True)
    a = a+1
    time.sleep(0.5)
    GPIO.output(17, False)
    a = a+1
    time.sleep(0.5)
GPIO.cleanup()
    