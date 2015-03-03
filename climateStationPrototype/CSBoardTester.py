# -*- coding: utf-8 -*-
import CSBoardManager
import CSDevice
import time


class CSBoardTester:
    """Tests out the components connected to the board"""

    def __init__(self):
        """Sets the board mode and default pins"""
        print "Preparing the BoardTester"

        self.leds = []
        self.dhts = []
        device1 = CSDevice.CSDevice()
        device1.setUp(device1.typeLED, device1.modeGpio, 21,
            -1, "First LED", "None")
        self.leds.append(device1)

        device2 = CSDevice.CSDevice()
        device2.setUp(device2.typeLED, device2.modeGpio, 26,
             -1, "Second LED", "None")
        self.leds.append(device2)

        device3 = CSDevice.CSDevice()
        device3.setUp(device3.typeDht, device3.modeGpio, 19,
             -1, "First DHT", "None")
        self.dhts.append(device3)

        device4 = CSDevice.CSDevice()
        device4.setUp(device4.typeLED, device4.modeGpio, 20,
             -1, "Second DHT", "None")
        self.dhts.append(device4)

        self.manager = CSBoardManager.CSBoardManager()
        self.manager.setDevices(self.leds)
        self.manager.appendDevices(self.dhts)

    def test(self):
        """Performs all the tests available in this class"""
        self.testLeds()
        time.sleep(0.5)
        self.testDhts()

    def testLeds(self):
        """ This will test LEDs on default ports. Those ports are 21 and 26."""
        print "Testing LEDs"

        for led in self.leds:
            self.testLed(led)
        self.manager.cleanUp()

    def testLed(self, device):
        """Tests a single LED, mounted to a given pin"""
        print "  Testing LED on pin: {}. Will blink 10 times".format(device.pin)
        count = 10
        while count > 0:
            self.manager.setDeviceState(device, True)
            time.sleep(0.2)
            self.manager.setDeviceState(device, False)
            time.sleep(0.2)
            count = count - 1

    def testDhts(self):
        """Tests the DHT sensors"""
        print "Testing DHTs"
        for device in self.dhts:
            humidity, temperature = self.manager.deviceState(device)
            if humidity is not None and temperature is not None:
                print "  Testing DHT on pin: {0}, temperature: {1:0.1f}, " \
                "humidity: {2:0.1f}" \
                .format(device.pin, temperature, humidity)
            else:
                print "  Error: could not read from DHT sensor on pin:", \
                device.pin, "Please retry"
