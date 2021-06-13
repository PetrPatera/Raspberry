from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

"BCM - Numbers after GPIO / BOARD - Numbers on the desk"
GPIO.setmode(GPIO.BCM)

"SBW PCB"
GPIO.setup(14,GPIO.OUT)
LEDArrow = LED(14)

"SBW PCB"
GPIO.setup(15,GPIO.OUT)
LEDRed = LED(15)

"SBW PCB"
GPIO.setup(18,GPIO.OUT)
LEDS = LED(18)

"SBW PCB"
GPIO.setup(23,GPIO.OUT)
LEDD = LED(23)

"SBW PCB"
GPIO.setup(24,GPIO.OUT)
LEDN = LED(24)

"SBW PCB"
GPIO.setup(25,GPIO.OUT)
LEDR = LED(25)

"SBW PCB"
GPIO.setup(8,GPIO.OUT)
LEDBackground = LED(8)

class LED():

    def spi(self,cas_v_sekundach):
        self.cas_v_sekundach = cas_v_sekundach
        return sleep(self.cas_v_sekundach)

    def sipka_on(self):
        LEDArrow.on()
        return #print("Šipka - ON")

    def sipka_off(self):
        LEDArrow.off()
        return #print("Šipka - OFF")

    def sipka_blick(self,opakovani):
        self.opakovani = opakovani
        if opakovani <= 0:
                opakovani = 1
        for _ in range(opakovani):
            LEDArrow.on()
            sleep(0.1)
            LEDArrow.off()
            sleep(0.1)

        return print("Šipka - Blick ({0})".format(self.opakovani))

    def red_on(self):
        LEDRed.on()
        return #print("Red - ON")

    def red_off(self):
        LEDRed.off()
        return #print("Red - OFF")

    def s_on(self):
        LEDS.on()
        return #print("S - ON")

    def s_off(self):
        LEDS.off()
        return #print("S - OFF")

    def d_on(self):
        LEDD.on()
        return #print("D - ON")

    def d_off(self):
        LEDD.off()
        return #print("D - OFF")

    def n_on(self):
        LEDN.on()
        return #print("N - ON")

    def n_off(self):
        LEDN.off()
        return #print("N - OFF")

    def r_on(self):
        LEDR.on()
        return #print("R - ON")

    def r_off(self):
        LEDR.off()
        return #print("R - OFF")

    def bg_on(self):
        LEDBackground.on()
        return #print("Background - ON")

    def bg_off(self):
        LEDBackground.off()
        return #print("Background - OFF")

    def bg_all_on(self):
        self.sipka_on()
        self.bg_on()
        return #print("Všechno podsvícení zapnuto")

    def bg_all_off(self):
        self.sipka_off()
        self.bg_off()
        return #print("Všechno podsvícení zhasnuto")

    def all_off(self):
        self.sipka_off()
        self.red_off()
        self.d_off()
        self.n_off()
        self.s_off()
        self.r_off()
        self.bg_all_off()

class Conditions(LED):

    def mensiNez(self,cislo):
        self.cislo = cislo
        if cislo <10:
            self.r_on()
            self.spi(1)
            self.r_off()
            self.sipka_blick(cislo*5)
            self.spi(1)
            self.n_on()
            self.spi(1)
            self.n_off()
            return print("číslo mejší jak 10")
        else:
            return print("číslo větší jak 10")

    def blickniBG(self):
        pocet_opakovani = 15 #int(input("Prosím vložce počet opakování: "))
        for _ in range(pocet_opakovani):
            self.sipka_on()
            sleep(0.1)
            self.sipka_off()
            sleep(0.1)
            self.red_on()
            sleep(0.1)
            self.red_off()
            sleep(0.1)
        return print("Počet bliknutí - {}x".format(pocet_opakovani))




