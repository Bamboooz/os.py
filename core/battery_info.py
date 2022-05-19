import psutil
import sys
from core.exception import *


def battery_percentage():
    if sys.platform == 'win32' or 'linux':
        battery = psutil.sensors_battery()
        percent = str(battery.percent)
        return percent + '%'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def is_plugged_in():
    if sys.platform == 'win32' or 'linux':
        battery = psutil.sensors_battery()
        return battery.power_plugged
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def battery_time_left():
    if sys.platform == 'win32' or 'linux':
        if is_plugged_in():
            return battery_plugged_error()
        else:
            return str(round(psutil.sensors_battery().secsleft / 60 / 60)) + 'h'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()
