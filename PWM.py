import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LedPlus = 5
GPIO.setup(LedPlus, GPIO.OUT)
led = GPIO.PWM(LedPlus, 50)
led.start(0)

#SpinServo = 12
#GPIO.setup(SpinServo, GPIO.OUT)
#servo = GPIO.PWM(SpinServo, 50) # PWM s frekvencí 50Hz
#servo.start(2.5)

class LED():

    def __init__(self):
        pass

    def plynula_zmena(self):
        for n in range(100):
            led.ChangeDutyCycle(n)
            sleep(0.03)
        for n in range(100):
            led.ChangeDutyCycle(100-n-1)
            sleep(0.02)

class Servo():

    def __init__(self):
        SpinServo = 12
        GPIO.setup(SpinServo, GPIO.OUT)
        self.servo = GPIO.PWM(SpinServo, 50)  # PWM s frekvencí 50Hz
        self.servo.start(2.5)

    def nastaveniUhlu(self, uhel):
        self.uhel = uhel
        sirkaImpulzu = uhel/18+2
        self.servo.ChangeDutyCycle(sirkaImpulzu)
        sleep(0.2)

    def akceCLOSE(self, uhel = 60):
        self.uhel = uhel
        sirkaImpulzu = uhel / 18 + 2
        self.servo.ChangeDutyCycle(sirkaImpulzu)
        sleep(0.15)

    def akceOPEN(self, uhel = 10):
        self.uhel = uhel
        sirkaImpulzu = uhel / 18 + 2
        self.servo.ChangeDutyCycle(sirkaImpulzu)
        sleep(0.18)

    def akceMAX(self, uhel = 100):
        self.uhel = uhel
        sirkaImpulzu = uhel / 18 + 2
        self.servo.ChangeDutyCycle(sirkaImpulzu)
        sleep(0.2)
