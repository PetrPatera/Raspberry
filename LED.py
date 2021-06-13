
from gpiozero import LED
from time import sleep

led = LED(21)

while True:
        #print("Start")
        #led.on()
        #sleep(1)
        #print("OFF")
        #led.off()
        #sleep(1)
        print("BLINK")
        led.blink()
