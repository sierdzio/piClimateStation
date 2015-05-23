# -*- coding: utf-8 -*-
import CSBoardManager
from time import sleep
import logging


class CSBoardTester:
    """Tests out the components connected to the board"""

    config = None
    manager = None

    def __init__(self, config):
        """Sets the board mode and default pins"""
        logging.info("Preparing the BoardTester")
        self.manager = CSBoardManager.CSBoardManager()
        self.config = config

    def test(self):
        """Performs all the tests available in this class"""
        if self.config is None:
            logging.error("Can't start the test when CSConfig is not "
                "initialized")
            return

        if self.config.devices is None or len(self.config.devices) == 0:
            logging.error("Can't start the test when device list is empty")

        self.manager.setDevices(self.config.devices)
        self.printDevices()
        self.testDevices()

    def printDevices(self):
        """Prints information about all devices undergoing the test"""
        logging.info("Devices taking part in this test:")
        for device in self.manager.devices:
            logging.info(device.toString())

    def testDevices(self):
        """ This will test devices added to the list"""
        logging.info("Testing Devices")

        for device in self.manager.devices:
            self.testDevice(device)
        self.manager.cleanUp()

    def testDevice(self, device):
        """Tests a single deivce"""
        logging.info("  Testing Device on pin: {}".format(device.pin))

        if not device.isValid():
            logging.info("    Device is not valid!")
            return

        if device.hasIndicator():
            count = 2
            logging.info("    Indicator LED will blink for {} seconds".
                format(count))
            device.toggleIndicator()
            sleep(count)
            device.toggleIndicator()

        # Toggle a switch
        if device.numberOfInputs() is 1:
            count = 5
            logging.info("    The device will be toggled repeatedly {} times"
                .format(count))
            while count > 0:
                device.setState(1)
                sleep(0.2)
                device.setState(0)
                sleep(0.2)
                count -= 1

        if device.numberOfOutputs() is 2:
            logging.info("    2 outputs detected. Reading...")
            humidity, temperature = device.state()
            if humidity is not None and temperature is not None:
                logging.info("    Testing DHT on pin: {0}, temperature: "
                    "{1:0.1f}, humidity: {2:0.1f}"
                    .format(device.pin, temperature, humidity))
            else:
                logging.info("    Error: could not read from DHT sensor on "
                    "pin:", device.pin, "Please retry")
