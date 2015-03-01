try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error could not import RPi.GPIO. You need to run as root, or "
        "install the module")

try:
    import Adafruit_DHT as DHT
except RuntimeError:
    print("Error: could not import Adafruit_DHT module. Please install it")

import time


class BoardTester:
    """Tests out the components connected to the board"""

    def __init__(self):
        """Sets the board mode and default pins"""
        print("Preparing the BoardTester")
        GPIO.setmode(GPIO.BCM)
        self.ledPins = [21, 26]
        self.dhtPins = [19, 20]

    def test(self):
        """Performs all the tests available in this class"""
        self.testLeds()
        time.sleep(0.5)
        self.testDht()

    def testLeds(self):
        """ This will test LEDs on default ports. Those ports are 21 and 26."""
        print("Testing LEDs")

        for pin in self.ledPins:
            self.testLed(pin)

    def testLed(self, pin):
        """Tests a single LED, mounted to a given pin"""
        print"Testing LED on pin: ", pin, ". Will blink 10 times"
        GPIO.setup(pin, GPIO.OUT)
        count = 10
        while count > 0:
            GPIO.output(pin, 1)
            time.sleep(0.2)
            GPIO.output(pin, 0)
            time.sleep(0.2)
            count = count - 1
        GPIO.cleanup(pin)

    def testDht(self):
        """Tests the DHT sensors"""
        for pin in self.dhtPins:
            humidity, temperature = DHT.read_retry(DHT.AM2302, pin)
            if humidity is not None and temperature is not None:
                print "Testing DHT on pin: {}".format(pin), \
                ", temperature: {0:0.1f}, humidity: {0:0.1f}" \
                .format(temperature, humidity)
            else:
                print "Error: could not read from DHT sensor on pin:", pin, \
                "Please retry"
