# -*- coding: utf-8 -*-
from CSBoardTester import CSBoardTester
import argparse

parser = argparse.ArgumentParser(description="Raspberry Pi Climate Station "
        "- prototype. Project maintains partial Python 3 compatibility - that "
        "is, you can run the simulation using Python 2 or Python 3. If you "
        "notce any problems here, please notify the developers. However, due "
        "to use of external libraries, Python 3 is not supported in real "
        "device mode, when connected to GPIO. Sorry about that.")

parser.add_argument('--simulated', dest="simulated", action="store_true",
    help="run the test in simulated mode - using the "
    "simulatedDevices.ini file as device list")

# TODO: add more logging options (ability to store measurements in a separate
# file; store device info separately; errors; timestamps)

parser.add_argument('-s', '--sensor-out-file', dest="sensorOutFile", type=str,
    help="path to file where sensor output should be written")

parser.add_argument('-o', '--out-file', dest="outFile", type=str,
    help="path to file where all remaining output should be written (device "
    "list, warnings, errors, runtime messages)")

parser.add_argument('-so', '--combined-out', dest="combinedOut", type=str,
    help="combination of -s and -o . Path to file where all output (sensor data"
    ", runtime messages, device list, warnings, errors, etc.) "
    "should be written")

args = parser.parse_args()
tester = CSBoardTester()

if args.simulated:
    tester.loadDevices("simulatedDevices.ini")
else:
    tester.loadDevices("realDevices.ini")

tester.test()
