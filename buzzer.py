import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=7

GPIO.setup(buzzer,GPIO.OUT)
try:
    while True:
        GPIO.output(buzzer,True)
        time.sleep(0.5)
        GPIO.output(buzzer,False)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    pass
