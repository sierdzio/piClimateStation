# -*- coding: utf-8 -*-
from CSBoardTester import CSBoardTester
from CSConfig import CSConfig
from sys import argv

tester = CSBoardTester()

if "-h" in argv or "--help" in argv:
    print("Raspberry Pi Climate Station - prototype\n\n"
        "By default, it runs a test in GPIO mode - and requires a properly"
        "connected and set-up Raspberry Pi to work. Please pass '-s' or"
        "'--simulated' to run the test in simulated mode - using the "
        "simulatedDevices.ini file as device list.\n\n"
        "Project maintains partial Python 3 compatibility - that is, you can "
        "run the simulation using Python 2 or Python 3. If you notce any "
        "problems here, please notify the developers. However, due to use of "
        "external libraries, Python 3 is not supported in real device mode, "
        "when connected to GPIO. Sorry about that.")
else:
    if "-s" in argv or "--simulated" in argv:
        tester.loadDevices("simulatedDevices.ini")
    elif "-t" in argv:
        tester.loadDevices("simulatedDevices.ini")
    else:
        tester.loadDevices("realDevices.ini")
    tester.test()
    outFile = "out/deviceSavingTest.ini"
    print("Testing INI file saving: current file list will be saved to {}"
        .format(outFile))
    config = CSConfig()
    config.saveDevices(tester.manager.devices, outFile)
