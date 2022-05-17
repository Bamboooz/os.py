import psutil
import sys
from core.exception import *


def battery_percentage():
    if sys.platform == 'win32':
        battery = psutil.sensors_battery()
        percent = str(battery.percent)
        return percent + '%'
    else:
        return unsupported_exception()


def is_plugged_in():
    if sys.platform == 'win32':
        battery = psutil.sensors_battery()
        return battery.power_plugged
    else:
        return unsupported_exception()


def battery_time_left():
    if sys.platform == 'win32':
        battery = psutil.sensors_battery()
        time = str(round(battery.secsleft / 60 / 60)) + 'h'
        if not time == 'Oh':
            return time
        else:
            if is_plugged_in():
                battery_plugged_error()
            else:
                no_battery_left_error()
    else:
        return unsupported_exception()
