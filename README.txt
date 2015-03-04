Raspberry Pi climate station (temporary name)
Copyright (c) 2015, Tomasz Siekierda, sierdzio@gmail.com

This project is Free Software, distributed under GPL v3 license. The project is in it's early stages and all the information contained here, including project name and license, can change in the future!

This project currently only consists of a basic prototype that does not even work. If you've got here looking for a ready-made solution, you should consider:
 a) waiting for the code to mature (will take a long time)
 b) searching for some other project

This project relies on Adafruit's DHT library: https://github.com/adafruit/Adafruit_Python_DHT.git

To install that library, do this (Debian):
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git libdht
    cd libdht
    sudo apt-get update
    sudo apt-get install build-essential python2-dev
    sudo python2 setup.py install