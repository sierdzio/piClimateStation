# -*- coding: utf-8 -*-
import CSBoardManager
import CSConfig
from time import sleep


class CSBoardTester:
    """Tests out the components connected to the board"""

    def __init__(self):
        """Sets the board mode and default pins"""
        print("Preparing the BoardTester")
        self.manager = CSBoardManager.CSBoardManager()

    def loadDevices(self, fileName):
        """Loads a list of devices from an INI file"""
        config = CSConfig.CSConfig()
        devices = config.loadDevices(fileName)
        self.manager.setDevices(devices)

    def test(self):
        """Performs all the tests available in this class"""
        self.printDevices()
        self.testDevices()

    def printDevices(self):
        """Prints information about all devices undergoing the test"""
        print("Devices taking part in this test:")
        for device in self.manager.devices:
            print(device.toString())

    def testDevices(self):
        """ This will test devices added to the list"""
        print("Testing Devices")

        for device in self.manager.devices:
            self.testDevice(device)
        self.manager.cleanUp()

    def testDevice(self, device):
        """Tests a single deivce"""
        print("  Testing Device on pin: {}".format(device.pin))

        if not device.isValid():
            print("    Device is not valid!")
            return

        if device.hasIndicator():
            count = 2
            print("    Indicator LED will blink for {} seconds".format(count))
            device.toggleIndicator()
            sleep(count)
            device.toggleIndicator()

        # Toggle a switch
        if device.numberOfInputs() is 1:
            count = 5
            print("    The device will be toggled repeatedly {} times"
                .format(count))
            while count > 0:
                device.setState(1)
                sleep(0.2)
                device.setState(0)
                sleep(0.2)
                count = count - 1

        if device.numberOfOutputs() is 2:
            print("    2 outputs detected. Reading...")
            humidity, temperature = device.state()
            if humidity is not None and temperature is not None:
                print("    Testing DHT on pin: {0}, temperature: {1:0.1f}, "
                "humidity: {2:0.1f}"
                .format(device.pin, temperature, humidity))
            else:
                print("    Error: could not read from DHT sensor on pin:",
                device.pin, "Please retry")
