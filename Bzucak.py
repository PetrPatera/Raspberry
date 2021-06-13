from gpiozero import Buzzer
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

"Připojení buzzeru"
GPIO.setup(17,GPIO.OUT)
Bzucak = Buzzer(17)

class Noise():

    def bzucakOpakovani(self, opakovani):
        self.opakovani = opakovani
        for _ in range(opakovani):
            Bzucak.on()
            sleep(0.25)
            Bzucak.off()
            sleep(0.25)

    def opakovaneBzuceni10(self):
        for _ in range(10):
            Bzucak.on()
            sleep(0.1)
            Bzucak.off()
            sleep(0.1)

    def konecBzuceni(self):
        Bzucak.off()

    def bzuceniPodminka(self, podminka):
        self.podminka = podminka
        while podminka:
            Bzucak.on()
            sleep(0.2)
            Bzucak.off()
            sleep(0.2)

