# -*- coding: utf-8 -*-
import CSBoardManager
import time


class CSBoardTester:
    """Tests out the components connected to the board"""

    def __init__(self):
        """Sets the board mode and default pins"""
        print "Preparing the BoardTester"
        self.outputs = [21, 26]
        self.inputs = [19, 20]
        self.manager = CSBoardManager.CSBoardManager()
        self.manager.setDataSource(self.manager.GPIO)
        print "Data source used for this test is", \
        self.manager.getDataSourceType()

    def test(self):
        """Performs all the tests available in this class"""
        self.testLeds()
        time.sleep(0.5)
        self.testDhts()

    def testLeds(self):
        """ This will test LEDs on default ports. Those ports are 21 and 26."""
        print "Testing LEDs"

        for pin in self.outputs:
            self.testLed(pin)
        self.manager.cleanUp()

    def testLed(self, pin):
        """Tests a single LED, mounted to a given pin"""
        print "  Testing LED on pin: {}. Will blink 10 times".format(pin)
        count = 10
        while count > 0:
            self.manager.setSwitchState(pin, True)
            time.sleep(0.2)
            self.manager.setSwitchState(pin, False)
            time.sleep(0.2)
            count = count - 1

    def testDhts(self):
        """Tests the DHT sensors"""
        print "Testing DHTs"
        for pin in self.inputs:
            humidity, temperature = self.manager.getSensorState(pin)
            if humidity is not None and temperature is not None:
                print "  Testing DHT on pin: {0}, temperature: {1:0.1f}, " \
                "humidity: {2:0.1f}" \
                .format(pin, temperature, humidity)
            else:
                print "  Error: could not read from DHT sensor on pin:", pin, \
                "Please retry"
