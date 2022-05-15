import os
import subprocess
import sys
import uuid
from core.exception import *


def motherboard_model():
    if sys.platform == 'win32':
        model = subprocess.check_output('wmic baseboard get product').decode().split('\n')[1].strip()
        return model
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return os.system('cat /sys/devices/virtual/dmi/id/board_name')
    else:
        return unsupported_exception()


def motherboard_manufacturer():
    if sys.platform == 'win32':
        manufacturer = subprocess.check_output('wmic baseboard get Manufacturer').decode().split('\n')[1].strip()
        return manufacturer
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return os.system('cat /sys/devices/virtual/dmi/id/board_vendor')
    else:
        return unsupported_exception()


def motherboard_serial_number():
    if sys.platform == 'win32':
        serial_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        return serial_id
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        dmidecode = os.popen('sudo -S dmidecode -t system | grep Serial').read()
        return dmidecode.replace('Serial Number: ', '').replace('	', '')
    else:
        return unsupported_exception()


def motherboard_version():
    if sys.platform == 'win32':
        version = subprocess.check_output('wmic baseboard get version').decode().split('\n')[1].strip()
        return version
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        dmidecode = os.popen('sudo -S dmidecode -t 2').read()
        for line in str(dmidecode).splitlines():
            if 'Version' in line:
                return line.replace('Version: ', '').replace('	', '')
    else:
        return unsupported_exception()


def motherboard_node():
    if sys.platform == 'win32' or 'linux':
        return uuid.getnode()
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()
