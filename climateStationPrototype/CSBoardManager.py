# -*- coding: utf-8 -*-
import CSBoardSimulator
import CSBoardGpio


class CSBoardManager:
    """Base class for managing connection between the board and sensors,
    switches etc."""

    GPIO = "GPIO"
    Simulator = "Simulator"

    def __init__(self):
        """Prepares the board manager"""
        self.inputs = []
        self.outputs = []
        self.dataSource = None
        self.dataSourceType = "None"

    def setDataSource(self, source):
        """Sets the data source to either real GPIO or simulator"""
        if source is self.Simulator:
            self.dataSource = CSBoardSimulator.CSBoardSimulator()
            self.dataSourceType = source
        elif source is self.GPIO:
            self.dataSource = CSBoardGpio.CSBoardGpio()
            self.dataSourceType = source
        else:
            self.dataSource = None
            self.dataSourceType = "None"

    def getDataSourceType(self):
        """Returns the type of data source currently in use"""
        return self.dataSourceType

    def appendInputs(self, inputs):
        """Appends new inputs to the internal list. Existing ones are
        not being replaced"""
        self.inputs.append(inputs)

    def appendOutputs(self, outputs):
        """Appends new outputs to the internal list. Existing ones are
        not being replaced"""
        self.outputs.append(outputs)

    def setInputs(self, inputs):
        """Sets the input pin list. All previous entries are removed"""
        self.inputs = inputs

    def setOutputs(self, outputs):
        """Sets the output pin list. All previous entries are removed"""
        self.outputs = outputs

    def getSensorState(self, pin):
        """Returns the values reported by given sensor.
        Does nothing if data source is invalid"""
        if self.dataSourceType is self.Simulator \
        or self.dataSourceType is self.GPIO:
            return self.dataSource.getSensorState(pin)

    def setSwitchState(self, pin, state):
        """Sets the state of a single pin. It can turn on a LED or a switch.
        Does nothing if data source is invalid"""
        if self.dataSourceType is self.Simulator \
        or self.dataSourceType is self.GPIO:
            self.dataSource.setSwitchState(pin, state)
