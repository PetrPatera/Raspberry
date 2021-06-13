import RPi.GPIO as GPIO
from time import sleep
from SBW import LED
from SBW import Conditions
from Klavesnice import Klavesnice
#from Teplomer import Teplomer
from Klavesnice2 import AutomatickaKlavesnice
from Bzucak import Noise
from RGB import RGBLED

GPIO.setmode(GPIO.BCM)

class Hlavni_kod():

    def __init__(self):
        self.led = LED()
        self.podminky = Conditions()
        self.noise = Noise()
        self.klavesnice = Klavesnice()
#        self.teplomer = Teplomer()
        self.automatickaKlavesnice = AutomatickaKlavesnice()
        self.rgb = RGBLED()

    def vyberProgramu(self):
        textMenu = """Vítejte v menu:\n 
        1) Teploměr - ODPOJENO
        2) Blikni
        3) Bzučák
        4) Volný průjezd\n
        5) Exit\n"""

        coChceme = int((input(textMenu)))

        if coChceme == 1:
            pass
#            self.teplomer.read_temp_print()
        elif coChceme == 2:
            self.podminky.blickniBG()
        elif coChceme == 3:
            vlozeneCislo = int(input("Prosím vložce počet opakování: "))
            self.noise.bzucakOpakovani(vlozeneCislo)
        elif coChceme == 4:
            self.rgb.bilaRGB_BLICK()

        # ------   EXIT  -----
        elif coChceme == 5:
            GPIO.cleanup()
            exit()
        else:
            print("Prosím vyberte z menu")

while True:
    try:
        program = Hlavni_kod()
        program.vyberProgramu()

    except KeyboardInterrupt:
        GPIO.cleanup()