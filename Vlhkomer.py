import RPi.GPIO as GPIO
from time import sleep

Pinout = 2

GPIO.setmode(GPIO.BCM)

GPIO.setup(Pinout, GPIO.IN)
DigitalINPUT = GPIO.input(Pinout)

while True:
    GPIO.add_event_detect(DigitalINPUT, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    DigitalINPUT = GPIO.input(Pinout)
    sleep(1)
    if DigitalINPUT:
        print("Zalijte kytky")
    else:
        print("Vše je OK")

