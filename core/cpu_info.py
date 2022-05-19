import os.path
import sys
import psutil
import wmi
import cpuinfo
from core.exception import *


def cpu_model():
    if sys.platform == 'win32' or 'linux':
        return cpuinfo.get_cpu_info()['brand_raw']
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def cpu_clockspeed():
    if sys.platform == 'win32' or 'linux':
        return cpuinfo.get_cpu_info()['hz_actual_friendly']
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def cpu_architecture():
    if sys.platform == 'win32' or 'linux':
        return cpuinfo.get_cpu_info()['arch']
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def cpu_processor_number():
    if sys.platform == 'win32' or 'linux':
        return cpuinfo.get_cpu_info()['count']
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def cpu_usage():
    if sys.platform == 'win32' or 'linux':
        return str(psutil.cpu_percent()) + '%'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def cpu_temperature():
    if sys.platform == 'win32':
        w_temp = wmi.WMI(namespace="root\\wmi")
        return str(round((w_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0) - 273.15)) + 'C'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        temp = '/sys/devices/virtual/thermal/thermal_zone0/temp'
        if os.path.exists(temp):
            celsius = int(open(temp).read().strip()) / 1000
            return celsius
        else:
            return no_linux_temp_driver()
    else:
        return unsupported_exception()


def cpu_vendor_id():
    if sys.platform == 'win32' or 'linux':
        return cpuinfo.get_cpu_info()['vendor_id_raw']
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()
