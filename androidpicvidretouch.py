#!/usr/bin/python3
# Clément BRUGUERA 2021
# Set back POSIX time files properties for pictures and videos pulled
# from Android devices by adb. 

import sys
import os
from os import utime, stat
import time
from datetime import datetime
import re

try:
    path = str(sys.argv[1])
except:
    path = '.'
    print("No path given, using .")

timeformat = "%Y%m%d%H%M%S"
p = re.compile('.*([\d]{8})_([\d]{6}).*\..+\Z')


files = [f for f in os.listdir(path) if os.path.isfile(f)]
for f in files:
    timestamps = p.findall(f)
    if timestamps:
        picturecreationdate = timestamps[0][0]
        picturecreationtime = timestamps[0][1]
        picturefulltime = picturecreationdate + picturecreationtime
        newdate = datetime.strptime(picturefulltime, timeformat)
        newtimestamp = datetime.timestamp(newdate)
        os.utime(f, times=(newtimestamp, newtimestamp))
