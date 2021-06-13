import RPi.GPIO as GPIO
from time import sleep
#from Teplomer import Teplomer
from SBW import Conditions
from PWM import Servo
from RGB import RGBLED
from Bzucak import Noise

GPIO.setmode(GPIO.BCM)
Nr1Pin = 13
Nr2Pin = 6
Nr3Pin = 26
Nr4Pin = 19


"Klávesnice tlačítko 1"
GPIO.setup(Nr1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Nr1 = GPIO.input(Nr1Pin)

"Klávesnice tlačítko 2"
GPIO.setup(Nr2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Nr2 = GPIO.input(Nr2Pin)

"Klávesnice tlačítko 3"
GPIO.setup(Nr3Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Nr3 = GPIO.input(Nr3Pin)

"Klávesnice tlačítko 4"
GPIO.setup(Nr4Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Nr4 = GPIO.input(Nr4Pin)

class AutomatickaKlavesnice():

    def callback_Nr1(self):
        bzucakmuj = Noise()
        return bzucakmuj.opakovaneBzuceni10()

    def callback_Nr2(self):
        rgbmoje = RGBLED()
        return rgbmoje.bilaRGB_BLICK() #teplomermuj.read_temp_print()

    def callback_Nr3(self):
        servomoje = Servo()
        rgbmoje = RGBLED()
        servomoje.akceCLOSE(), rgbmoje.redRGBSemafor_on(), rgbmoje.greenRGB_off()
        return print("Závora zavřena")

    def callback_Nr4(self):
        servomoje = Servo()
        rgbmoje = RGBLED()
        servomoje.akceOPEN(), rgbmoje.redRGB_off(), rgbmoje.greenRGB_on()
        return print("Závora otevřena")

GPIO.add_event_detect(Nr1Pin, GPIO.RISING, callback=AutomatickaKlavesnice.callback_Nr1, bouncetime=500)
GPIO.add_event_detect(Nr2Pin, GPIO.RISING, callback=AutomatickaKlavesnice.callback_Nr2, bouncetime=500)
GPIO.add_event_detect(Nr3Pin, GPIO.RISING, callback=AutomatickaKlavesnice.callback_Nr3, bouncetime=500)
GPIO.add_event_detect(Nr4Pin, GPIO.RISING, callback=AutomatickaKlavesnice.callback_Nr4, bouncetime=500)