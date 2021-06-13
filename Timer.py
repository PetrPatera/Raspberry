#! /usr/bin/env python

# Simple clock program. Writes the exact time.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import LCD_drivers
from time import sleep
from _datetime import datetime
import time

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = LCD_drivers.Lcd()

try:
    casStart = time.time()
    casStartstr = time.strftime("%H:%M:%S", time.gmtime(casStart))
    print("Start in - ", casStartstr)
#    display.lcd_display_string("No time to waste", 1)  # Write line of text to first line of display
    casStart = time.time()
    while True:
        casNyni = time.time()
        casNynistr = time.strftime("%H:%M:%S", time.gmtime(casNyni+7200))
#        print("Konec - ", time.strftime("%H:%M:%S", time.gmtime(casNyni)))
        vysledek = casNyni - casStart
        casVypocet = time.strftime("%H:%M:%S", time.gmtime(vysledek))
        # Write just the time to the display
        display.lcd_display_string(casVypocet, 1)  # Write line of text to first line of display
        display.lcd_display_string(casNynistr, 2)
        # Uncomment the following line to loop with 1 sec delay
        # sleep(1)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear() 