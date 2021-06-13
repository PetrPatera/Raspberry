from gpiozero import Servo
import RPi.GPIO as GPIO
from time import sleep
pwm = GPIO.PWM(17,50)
pwm
"""servo.min()
sleep(1)
servo.mid()
sleep(1)
servo.max()
sleep(1)
"""


