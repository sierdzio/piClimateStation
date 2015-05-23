# -*- coding: utf-8 -*-
from time import sleep
import threading
import logging
from datetime import datetime


class CSDevice:
    """Stores information about a single device connected
    to GPIO"""

    # Type "enum"
    typeDht = "DHT"
    typeLED = "LED"
    typeSwitch = "Switch"
    typeNone = "None"

    # Mode "enum""
    modeGpio = "GPIO"
    modeSimulator = "Simulator"
    modeNone = "None"

    logger = logging.getLogger("Device")
    handler = logging.FileHandler('out/deviceReadings.log', 'a+', "UTF-8")

    def __init__(self):
        """Initializes the device"""

        self.validTypes = [self.typeDht, self.typeLED, self.typeSwitch]
        self.validModes = [self.modeGpio, self.modeSimulator]

        # Logging to file
        self.logger.addHandler(self.handler)

        # Device type
        self.type = self.typeNone

        # Device mode
        self.mode = self.modeNone
        self._dataSource = None

        # Does the device have a LED indicator (and it's pin)
        self.indicatorPin = -1
        self.indicatorState = False
        self.threadStopEvent = threading.Event()
        self._indicatorThread = None

        # Device's GPIO pin number (BCM!)
        self.pin = -1

        # Optional:
        # device name
        self.name = self.typeNone
        # device description
        self.description = self.typeNone

    # TODO: handle bad typing in type and mode (wrong case, alternatve names)
    # (partially done: for modes)
    def setUp(self, type, mode, pin, indicatorPin, name, description):
        """Allows to quickly set up a device object"""
        if type in self.validTypes:
            self.type = type
        self.setDataMode(mode)
        self.pin = pin
        self.indicatorPin = indicatorPin
        self.name = name
        self.description = description

    def isValid(self):
        """Returns true if the device is valid, that is when
        the mode is set and the pin number is correct"""
        if (self.mode == self.modeSimulator
        or self.mode == self.modeGpio) \
        and (self.pin >= 0 and self.pin <= 31):
            return True
        else:
            return False

    def cleanUp(self):
        """Makes sure the GPIO is left in a usable state"""
        if self.isValid():
            self._dataSource.cleanUp()

    def state(self):
        """Returns the values reported by given sensor.
        Or None if data source is invalid"""
        if self.isValid():
            humidity, temperature = self._dataSource.getSensorState(self.pin)
            self.logger.info("%s;%s;%s", humidity, temperature,
                datetime.utcnow())
            return (humidity, temperature)
        else:
            return None

    def setState(self, state):
        """Sets the state of a device. It can turn on a LED or a switch.
        Or None if data source is invalid"""
        if self.isValid():
            self._dataSource.setSwitchState(self.pin, state)

    def hasIndicator(self):
        """Returns true if the control contains an indicator LED"""
        if self.indicatorPin >= 0 and self.indicatorPin <= 31:
            return True
        else:
            return False

    def _indicatorToggler(self, event, source, pin):
        tempState = False
        while not event.is_set():
            source.setSwitchState(pin, tempState)
            sleep(0.2)
            tempState = not tempState

    def toggleIndicator(self):
        """Turns the indicator LED on or off"""
        if self.hasIndicator() and self.isValid():
            self.indicatorState = not self.indicatorState

            if self._indicatorThread:
                self.threadStopEvent.set()

            if not self.indicatorState:
                return

            self._indicatorThread = threading.Thread(
                args=(self.threadStopEvent, self._dataSource,
                     self.indicatorPin),
                target=self._indicatorToggler)
            self.threadStopEvent.clear()
            self._indicatorThread.start()

    def numberOfInputs(self):
        """Returns the number of inputs this device has. An input is something
        we can change, like LED state, a switch, and so on"""
        result = 1
        if self.type == self.typeDht or self.type == self.typeNone:
            result = 0
        return result

    def numberOfOutputs(self):
        """Returns the number of outputs. An output is something that
        returns a value, like a temperature sensor"""
        result = 0
        if self.type == self.typeDht:
            result = 2
        return result

    def setDataMode(self, mode):
        """Sets the data source to either real GPIO or simulator"""
        if mode.lower() == self.modeSimulator.lower():
            import CSBoardSimulator
            self._dataSource = CSBoardSimulator.CSBoardSimulator()
            self.mode = self.modeSimulator
        elif mode.lower() == self.modeGpio.lower():
            import CSBoardGpio
            self._dataSource = CSBoardGpio.CSBoardGpio()
            self.mode = self.modeGpio
        else:
            self._dataSource = None
            self.mode = self.modeNone

    def toString(self):
        """Returns a well-formatted, human readable string containing all Device
        infomation currently stored in the object"""
        return "Device:\n  Name: '{}'\n  Description: '{}'\n  Pin {}\n  LED " \
        "indicator pin: {}\n  Type: {}\n  Data access mode: {}\n  " \
        .format(self.name, self.description, self.pin, self.indicatorPin,
        self.type, self.mode)
