# -*- coding: utf-8 -*-
from sys import version_info

if version_info.major < 3:
    import ConfigParser
    import codecs
else:
    import configparser
import CSDevice
from os import path


class CSConfig:
    """Saves and loads climate station configuration, including a device list"""

    devices = []

    # Output file section
    sensorOutFilePath = "out/readings.log"
    outFilePath = "out/out.log"

    # If sensorOutFilePath and outFilePath are the same, the output is combined
    # and put into a single file
    combined = False

    def __init__(self):
        """Does nothing"""
        pass

    # TODO: check for errors, exceptions
    def loadDevices(self, fileName):
        """Loads a list of devices from file with fileName. Config files
        and device list files are separate to allow greater flexibility"""
        parser = None
        if version_info.major < 3:
            parser = ConfigParser.ConfigParser()
        else:
            parser = configparser.ConfigParser()
        filePath = path.join(path.dirname(__file__), fileName)
        parser.read(filePath)
        print("Loading devices from file '{}'".format(filePath))
        self.devices = []
        for section in parser.sections():
            device = CSDevice.CSDevice()
            device.setUp(
                parser.get(section, "type"),
                parser.get(section, "mode"),
                parser.getint(section, "pin"),
                parser.getint(section, "indicatorpin"),
                parser.get(section, "name"),
                parser.get(section, "description"))
            self.devices.append(device)
        return self.devices

    # TODO: check for errors, exceptions
    def saveDevices(self, devices, fileName):
        """Saves devices to a file under fileName"""
        parser = None
        if version_info.major < 3:
            parser = ConfigParser.ConfigParser()
        else:
            parser = configparser.ConfigParser()
        filePath = path.join(path.dirname(__file__), fileName)
        index = 0
        for device in devices:
            section = "Device" + str(index)
            parser.add_section(section)
            parser.set(section, "type", device.type)
            parser.set(section, "mode", device.mode)
            parser.set(section, "pin", str(device.pin))
            parser.set(section, "indicatorpin", str(device.indicatorPin))
            parser.set(section, "name", device.name)
            parser.set(section, "description", device.description)
            index = index + 1
        if version_info.major < 3:
            parser.write(codecs.open(filePath, 'wt', encoding='utf-8'))
        else:
            parser.write(open(filePath, 'wt', encoding='utf-8'))
