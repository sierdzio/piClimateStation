# -*- coding: utf-8 -*-
from CSBoardTester import CSBoardTester
from CSConfig import CSConfig
import argparse

parser = argparse.ArgumentParser(description="Raspberry Pi Climate Station "
        "- prototype. Project maintains partial Python 3 compatibility - that "
        "is, you can run the simulation using Python 2 or Python 3. If you "
        "notce any problems here, please notify the developers. However, due "
        "to use of external libraries, Python 3 is not supported in real "
        "device mode, when connected to GPIO. Sorry about that.")

parser.add_argument('-s', '--simulated', dest="simulated", action="store_true",
    help="run the test in simulated mode - using the "
    "simulatedDevices.ini file as device list")

parser.add_argument('-o', '--out', dest="outFile", type=str,
    default="out/deviceSavingTest.ini",
    help="save current device list to out directory")

parser.add_argument('-t', '--test-file-saving', dest="testFS",
    action="store_true", help="specify custom output file name")

# TODO: add more logging options (ability to store measurements in a separate
# file; store device info separately; errors; timestamps)

args = parser.parse_args()
tester = CSBoardTester()

if args.simulated:
    tester.loadDevices("simulatedDevices.ini")
else:
    tester.loadDevices("realDevices.ini")
tester.test()

if args.testFS:
    print(("Testing INI file saving: current file list will be saved to {}"
    .format(args.outFile)))
    config = CSConfig()
    config.saveDevices(tester.manager.devices, args.outFile)
