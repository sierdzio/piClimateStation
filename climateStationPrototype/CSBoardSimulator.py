# -*- coding: utf-8 -*-
import random


class CSBoardSimulator:
    """Provides simulation for CSBOardManager class"""

    def __init__(self):
        """Does nothing"""
        pass

    def cleanUp(self):
        """Makes sure the GPIO is left in a usable state"""
        print("[Sim] Cleaning up a pin")

    def getSensorState(self, pin):
        """Returns some random state"""
        result = (random.random(), random.random() * 3)
        print("[Sim] Returning sensor state for pin {0}: {1:0.1f}, {2:0.1f}"
            .format(pin, result[0], result[1]))
        return result

    def setSwitchState(self, pin, state):
        """Simulates setting a state"""
        print("[Sim] Switching pin {} to state {}".format(pin, state))