# -*- coding: utf-8 -*-
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error could not import RPi.GPIO. You need to run as root, or "
    "install the module")

try:
    from Adafruit_DHT import common as DHT
except RuntimeError:
    print("Error: could not import Adafruit_DHT module. Please install it")


class CSBoardGpio:
    """Communicates with real GPIO devices"""

    def __init__(self):
        """Prepares the board for communication"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def cleanUp(self):
        """Makes sure the GPIO is left in a usable state"""
        GPIO.cleanup()

    def getSensorState(self, pin):
        """Attempts to read from DHT sensor on given pin"""
        return DHT.read_retry(DHT.AM2302, pin)

    def setSwitchState(self, pin, state):
        """Sets the state of a single pin. It can turn on a LED or a switch"""
        GPIO.setup(pin, GPIO.OUT)
        if state is True:
            GPIO.output(pin, 1)
        else:
            GPIO.output(pin, 0)