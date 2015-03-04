# -*- coding: utf-8 -*-
import CSBoardManager
import CSDevice
import time


class CSBoardTester:
    """Tests out the components connected to the board"""

    def __init__(self):
        """Sets the board mode and default pins"""
        print "Preparing the BoardTester"

        devices = []
        simulated = []
        device1 = CSDevice.CSDevice()
        device1.setUp(device1.typeDht, device1.modeGpio, 20,
            21, "First DHT device", "None")
        devices.append(device1)

        device2 = CSDevice.CSDevice()
        device2.setUp(device2.typeDht, device2.modeGpio, 19,
             26, "Second DHT device", "None")
        devices.append(device2)

        device22 = CSDevice.CSDevice()
        device22.setUp(device22.typeLED, device22.modeSimulator, 26,
             -1, "A LED", "Simulated LED")
        simulated.append(device22)

        self.manager = CSBoardManager.CSBoardManager()
        self.manager.setDevices(devices)
        self.manager.appendDevices(simulated)

    def test(self):
        """Performs all the tests available in this class"""
        self.printDevices()
        self.testDevices()

    def printDevices(self):
        """Prints information about all devices undergoing the test"""
        print "Devices taking part in this test:"
        for device in self.manager.devices:
            print device.toString()

    def testDevices(self):
        """ This will test devices added to the list"""
        print "Testing Devices"

        for device in self.manager.devices:
            self.testDevice(device)
        self.manager.cleanUp()

    def testDevice(self, device):
        """Tests a single deivce"""
        print "  Testing Device on pin: {}".format(device.pin)

        if not device.isValid():
            print "    Device is not valid!"

        if device.hasIndicator():
            print "    Indicator LED will blink 10 times"
            count = 10
            while count > 0:
                device.toggleIndicator()
                time.sleep(0.2)
                device.toggleIndicator()
                time.sleep(0.2)
                count = count - 1

        if device.numberOfInputs() is 1:
            print "    Input detected. Will blink 10 times"
            count = 10
            while count > 0:
                device.setState(1)
                time.sleep(0.2)
                device.setState(0)
                time.sleep(0.2)
                count = count - 1

        if device.numberOfOutputs() is 2:
            print "    2 outputs detected. Reading..."
            humidity, temperature = device.state()
            if humidity is not None and temperature is not None:
                print "    Testing DHT on pin: {0}, temperature: {1:0.1f}, " \
                "humidity: {2:0.1f}" \
                .format(device.pin, temperature, humidity)
            else:
                print "    Error: could not read from DHT sensor on pin:", \
                device.pin, "Please retry"
