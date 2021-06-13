import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RGB = [21,20,16]
frekvence = 100
"""for pin in RGB:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.PWM(pin, frekvence)
    GPIO.output(pin, 0)"""

class RGBLED():

    def __init__(self):
        for pin in RGB:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.PWM(pin, frekvence)
            GPIO.output(pin, 0)

    def mainCode(self):
        try:
            while(True):
                request = input("RGB-->")
                frekvence = int(input("Frekvence: "))
                print(type(frekvence))
                for pin in RGB:
                    GPIO.PWM(pin, frekvence)
                if (len(request) == 3):
                    GPIO.output(RGB[0], int(request[0]))
                    GPIO.output(RGB[1], int(request[1]))
                    GPIO.output(RGB[2], int(request[2]))

        except KeyboardInterrupt:
            GPIO.cleanup()

    def redRGB_on(self, hodnota = 1):
        GPIO.output(RGB[0], hodnota)
    def redRGBSemafor_on(self, hodnota=1):
        GPIO.output(RGB[0], hodnota)
        GPIO.output(RGB[1], 0)
        GPIO.output(RGB[2], 0)
    def redRGB_off(self, hodnota = 0):
        GPIO.output(RGB[0], hodnota)

    def greenRGB_on(self, hodnota = 1):
        GPIO.output(RGB[1], hodnota)
    def greenRGB_off(self, hodnota = 0):
        GPIO.output(RGB[1], hodnota)

    def blueRGB_on(self, hodnota = 1):
        GPIO.output(RGB[2], hodnota)
    def blueRGB_off(self, hodnota = 0):
        GPIO.output(RGB[2], hodnota)

    def bilaRGB_ON(self, hodnota = 1):
        GPIO.output(RGB[0], hodnota)
        GPIO.output(RGB[1], hodnota)
        GPIO.output(RGB[2], hodnota)
    def bilaRGB_OFF(self, hodnota = 0):
        GPIO.output(RGB[0], hodnota)
        GPIO.output(RGB[1], hodnota)
        GPIO.output(RGB[2], hodnota)

    def bilaRGB_BLICK(self):
        for _ in range (5):
            self.bilaRGB_ON()
            sleep(0.5)
            self.bilaRGB_OFF()
            sleep(0.5)


"""rgb = RGBLED()
while True:
    try:
        rgb.redRGB_on()
        sleep(0.5)
        rgb.redRGB_off()
        sleep(0.5)
        rgb.greenRGB_on()
        sleep(0.5)
        rgb.greenRGB_off()
        sleep(0.5)
        rgb.blueRGB_on()
        sleep(0.5)
        rgb.blueRGB_off()
        sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()"""