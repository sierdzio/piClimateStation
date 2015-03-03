# -*- coding: utf-8 -*-


class CSBoardManager:
    """Base class for managing connection between the board and sensors,
    switches etc."""

    def __init__(self):
        """Prepares the board manager"""
        self.devices = []

    # WARNING: this does not work - needs fixing!
    def appendDevices(self, inputs):
        """Appends new devices to the internal list. Existing ones are
        not being replaced"""
        self.devices = self.devices + inputs

    def setDevices(self, inputs):
        """Sets the devices list. All previous entries are removed"""
        self.devices = inputs

    def cleanUp(self):
        """Makes sure the GPIO is left in a usable state"""
        for device in self.devices:
            device.cleanUp()

    def deviceState(self, device):
        """Returns the values reported by given sensor"""
        return device.state()

    def setDeviceState(self, device, state):
        """Sets the state of a device. It can turn on a LED or a switch"""
        device.setState(state)
