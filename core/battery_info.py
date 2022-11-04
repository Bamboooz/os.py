import psutil
import sys
from core.exception import *


def battery_percentage():
    if sys.platform == 'win32':
        percent = str(psutil.sensors_battery().percent)
        return percent + '%'
    elif sys.platform == 'linux':
        try:
            percent = str(psutil.sensors_battery().percent)
            return percent + '%'
        except:
            print(no_linux_driver())
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def is_plugged_in():
    if sys.platform == 'win32':
        return psutil.sensors_battery().power_plugged
    elif sys.platform == 'linux':
        try:
            return psutil.sensors_battery().power_plugged
        except:
            print(no_linux_driver())
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def battery_time_left():
    if sys.platform == 'win32':
        if is_plugged_in():
            return 0
        else:
            return str(round(psutil.sensors_battery().secsleft / 60 / 60)) + 'h'
    elif sys.platform == 'linux':
        try:
            if is_plugged_in():
                return 0
            else:
                return str(round(psutil.sensors_battery().secsleft / 60 / 60)) + 'h'
        except:
            print(no_linux_driver())
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())
