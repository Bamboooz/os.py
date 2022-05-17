import sys
import psutil
import wmi
import cpuinfo
from core.exception import *


def cpu_model():
    if sys.platform == 'win32':
        return cpuinfo.get_cpu_info()['brand_raw']
    else:
        return unsupported_exception()


def cpu_clockspeed():
    if sys.platform == 'win32':
        return cpuinfo.get_cpu_info()['hz_actual_friendly']
    else:
        return unsupported_exception()


def cpu_architecture():
    if sys.platform == 'win32':
        return cpuinfo.get_cpu_info()['arch']
    else:
        return unsupported_exception()


def cpu_processor_number():
    if sys.platform == 'win32':
        return cpuinfo.get_cpu_info()['count']
    else:
        return unsupported_exception()


def cpu_usage():
    if sys.platform == 'win32':
        return str(psutil.cpu_percent()) + '%'
    else:
        return unsupported_exception()


def cpu_temperature():
    if sys.platform == 'win32':
        w_temp = wmi.WMI(namespace="root\\wmi")
        return str(round((w_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0) - 273.15)) + 'C'
    else:
        return unsupported_exception()


def cpu_vendor_id():
    if sys.platform == 'win32':
        return cpuinfo.get_cpu_info()['vendor_id_raw']
    else:
        return unsupported_exception()
