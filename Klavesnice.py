import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
"Klávesnice tlačítko 3"
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Nr3 = GPIO.input(26)

"Klávesnice tlačítko 4"
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Nr4 = GPIO.input(19)

"Klávesnice tlačítko 1"
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Nr1 = GPIO.input(13)

"Klávesnice tlačítko 2"
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Nr2 = GPIO.input(6)

class Klavesnice():

    def printStav(self):
        """
        Vyčte hodnotu z klávesnice
        :return: aktuální výsledek z klávesnice
        """
        if(GPIO.input(6) == 0):
            vysledek = 2
            sleep(0.5)
        elif(GPIO.input(13) == 0):
            vysledek = 1
            sleep(0.5)
        elif(GPIO.input(19) == 0):
            vysledek = 4
            sleep(0.5)
        elif(GPIO.input(26) == 0):
            vysledek = 3
            sleep(0.5)
        return print(vysledek)

    def vycitaniKlavesnice(self):
        """
        :param self:
        :return: Vrací dokola hodnotu z klávesnice
        """
        "Klávesnice tlačítko 3"

        while True:
            podminka = False
            if (GPIO.input(6) == 0):
                vysledek = 2
                sleep(0.5)
                podminka = True
            elif (GPIO.input(13) == 0):
                vysledek = 1
                sleep(0.5)
                podminka = True
            elif (GPIO.input(19) == 0):
                vysledek = 4
                sleep(0.5)
                podminka = True
            elif (GPIO.input(26) == 0):
                vysledek = 3
                sleep(0.5)
                podminka = True
            if podminka:
                print(vysledek)
                podminka = False
