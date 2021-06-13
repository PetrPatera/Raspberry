#! /usr/bin/env python

# Simple clock program. Writes the exact time.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
from builtins import dict

import LCD_drivers
from time import sleep
from smbus2 import SMBus, i2c_msg

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = LCD_drivers.Lcd()

class Lcd():

    def text_prvni_radek(self, text):
        self.text = str(text)
        return display.lcd_display_string(self.text,1)

    def text_druhy_radek(self, text):
        self.text = str(text)
        return display.lcd_display_string(self.text,2)

    def zapis_ctyri_byty(self, data):
        self.data = data
        display.lcd_write_four_bits(self.data)

    def vycistit(self):
        display.lcd_clear()

pokus = Lcd()
pokus.text_prvni_radek("Ahoj")
pokus.text_druhy_radek("Ne-e")
sleep(2)
pokus.zapis_ctyri_byty(0x01)
sleep(2)
pokus.text_prvni_radek("Nazdar")
pokus.text_druhy_radek("Ale jo")
sleep(2)
pokus.vycistit()