# -*- coding: utf-8 -*-
import CSBoardTester
from sys import argv

tester = CSBoardTester.CSBoardTester()

if "-h" in argv or "--help" in argv:
    print("Raspberry Pi Climate Station - prototype\n\n"
        "By default, it runs a test in GPIO mode - and requires a properly"
        "connected and set-up Raspberry Pi to work. Please pass '-s' or"
        "'--simulated' to run the test in simulated mode - using the "
        "simulatedDevices.ini file as device list")
else:
    if "-s" in argv or "--simulated" in argv:
        tester.loadDevices("simulatedDevices.ini")
    else:
        tester.loadDevices("realDevices.ini")
    tester.test()
