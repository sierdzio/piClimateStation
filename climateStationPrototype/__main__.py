# -*- coding: utf-8 -*-
from CSBoardTester import CSBoardTester
from CSConfig import CSConfig
import argparse
import logging

parser = argparse.ArgumentParser(description="Raspberry Pi Climate Station "
        "- prototype. Project maintains partial Python 3 compatibility - that "
        "is, you can run the simulation using Python 2 or Python 3. If you "
        "notce any problems here, please notify the developers. However, due "
        "to use of external libraries, Python 3 is not supported in real "
        "device mode, when connected to GPIO. Sorry about that. "
        "All measurements in this application are using metric (SI) units. "
        "The exception is temperature, which is always given in Celsius")

parser.add_argument('--simulated', dest="simulated", action="store_true",
    help="run the test in simulated mode - using the "
    "simulatedDevices.ini file as device list")

parser.add_argument('--silent-console', dest="silentConsole",
    action="store_true",
    help="do not print anything to the console. All output will be redirected "
        "to output files")

parser.add_argument('-s', '--sensor-out-file', dest="sensorOutFile", type=str,
    help="path to file where sensor output should be written")

args = parser.parse_args()

if args.silentConsole:
    logging.basicConfig(level=logging.CRITICAL)
else:
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S', level=logging.INFO)

config = CSConfig(args)
tester = CSBoardTester(config)

if args.simulated:
    config.loadDevices("simulatedDevices.ini")
else:
    config.loadDevices("realDevices.ini")

tester.test()
