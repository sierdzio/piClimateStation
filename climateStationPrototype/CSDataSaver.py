# -*- coding: utf-8 -*-


class CSDataSaver:
    """Polls attached devices and saves their data to a chosen medium, like
    file on the file system, DBUS interface, other storage"""

    def __init__(self):
        """Constructor"""
        self.destinations = []