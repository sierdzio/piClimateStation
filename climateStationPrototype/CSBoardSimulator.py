# -*- coding: utf-8 -*-
import random


class CSBoardSimulator:
    """Provides simulation for CSBOardManager class"""

    def __init__(self):
        """Does nothing"""
        pass

    def cleanUp(self):
        """Makes sure the GPIO is left in a usable state"""
        print "[Sim] Cleaning up a pin"

    def getSensorState(self, pin):
        """Returns some random state"""
        result = random() % 2
        print "[Sim] Returning sensor state for pin {}: {}".format(pin, result)
        return result

    def setSwitchState(self, pin, state):
        """Simulates setting a state"""
        print "[Sim] Switching pin {} to state {}".format(pin, state)