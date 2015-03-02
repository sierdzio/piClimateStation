# -*- coding: utf-8 -*-
import random


class CSBoardSimulator:
    """Provides simulation for CSBOardManager class"""

    def __init__(self):
        """Does nothing"""
        pass

    def cleanUp(self):
        """Makes sure the GPIO is left in a usable state"""
        pass

    def getSensorState(self, pin):
        """Returns some random state"""
        return random() % 2

    def setSwitchState(self, pin, state):
        """Simulates setting a state"""
        print "Switching pin {} to state {}".format(pin, state)