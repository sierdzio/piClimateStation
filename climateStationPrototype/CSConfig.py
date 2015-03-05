# -*- coding: utf-8 -*-
import ConfigParser
import CSDevice
from os import path


class CSConfig:
    """Saves and loads climate station configuration, including a device list"""

    def __init__(self):
        """Does nothing"""
        pass

    # TODO: check for errors, exceptions
    def loadDevices(self, fileName):
        """Loads a list of devices from file with fileName. Config files
        and device list files are separate to allow greater flexibility"""
        parser = ConfigParser.ConfigParser()
        filePath = path.join(path.dirname(__file__), fileName)
        parser.read(filePath)
        print("Loading devices from file '{}'".format(filePath))
        result = []
        for section in parser.sections():
            device = CSDevice.CSDevice()
            device.setUp(
                parser.get(section, "Type"),
                parser.get(section, "Mode"),
                parser.getint(section, "Pin"),
                parser.getint(section, "IndicatorPin"),
                parser.get(section, "Name"),
                parser.get(section, "Description"))
            result.append(device)
        return result

    # TODO: check for errors, exceptions
    def saveDevices(self, devices, fileName):
        """Saves devices to a file under fileName"""
        parser = ConfigParser.ConfigParser()
        index = 0
        for device in devices:
            section = "Device" + index
            parser.add_section(section)
            parser.set(section, "Type", device.type)
            parser.set(section, "Mode", device.mode)
            parser.set(section, "Pin", device.pin)
            parser.set(section, "IndicatorPin", device.indicatorPin)
            parser.set(section, "Name", device.name)
            parser.set(section, "Description", device.description)
            index = index + 1
        parser.write(open(fileName, 'wb'))
