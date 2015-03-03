# -*- coding: utf-8 -*-


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

    def __init__(self):
        """Initializes the device"""

        # Device type
        self.type = self.typeNone

        # Device mode
        self.mode = self.modeNone
        self._dataSource = None

        # Does the device have a LED indicator (and it's pin)
        self.hasIndicator = False
        self.indicatorPin = -1

        # Device's GPIO pin number (BCM!)
        self.pin = -1

        # Optional:
        # device name
        self.name = self.typeNone
        # device description
        self.description = self.typeNone

    def setUp(self, type, mode, pin, indicatorPin, name, description):
        """Allows to quickly set up a device object"""
        # TODO: check values for validity!
        self.type = type
        self.setDataMode(mode)
        self.pin = pin
        self.indicatorPin = indicatorPin
        self.name = name
        self.description = description

    def isValid(self):
        """Returns true if the device is valid, that is when
        the mode is set and the pin number is correct"""
        if (self.mode is self.modeSimulator
        or self.mode is self.modeGpio) \
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
            return self._dataSource.getSensorState(self.pin)
        else:
            return None

    def setState(self, state):
        """Sets the state of a device. It can turn on a LED or a switch.
        Or None if data source is invalid"""
        if self.isValid():
            self._dataSource.setSwitchState(self.pin, state)

    def toggleIndicator(self):
        """Turns the indicator LED on or off"""
        pass

    def setDataMode(self, mode):
        """Sets the data source to either real GPIO or simulator"""
        if mode is self.modeSimulator:
            import CSBoardSimulator
            self._dataSource = CSBoardSimulator.CSBoardSimulator()
            self.mode = self.modeSimulator
        elif mode is self.modeGpio:
            import CSBoardGpio
            self._dataSource = CSBoardGpio.CSBoardGpio()
            self.mode = self.modeGpio
        else:
            self._dataSource = None
            self.mode = self.modeNone
