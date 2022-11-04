import os
import subprocess
import uuid
import sys
from core.exception import *


def motherboard_model():
    if sys.platform == 'win32':
        model = subprocess.check_output('wmic baseboard get product').decode().split('\n')[1].strip()
        return model
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        try:
            return os.system('cat /sys/devices/virtual/dmi/id/board_name')
        except:
            print(unknown_exception())
    else:
        print(unsupported_exception())


def motherboard_manufacturer():
    if sys.platform == 'win32':
        manufacturer = subprocess.check_output('wmic baseboard get Manufacturer').decode().split('\n')[1].strip()
        return manufacturer
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        try:
            return os.system('cat /sys/devices/virtual/dmi/id/board_vendor')
        except:
            print(unknown_exception())
    else:
        print(unsupported_exception())


def motherboard_serial_number():
    if sys.platform == 'win32':
        serial_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        return serial_id
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        try:
            return os.system('cat /sys/class/dmi/id/board_serial')
        except:
            print(unknown_exception())
    else:
        print(unsupported_exception())


def motherboard_version():
    if sys.platform == 'win32':
        version = subprocess.check_output('wmic baseboard get version').decode().split('\n')[1].strip()
        return version
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        try:
            return os.system('cat /sys/class/dmi/id/board_version:')
        except:
            print(unknown_exception())
    else:
        print(unsupported_exception())


def motherboard_node():
    if sys.platform == 'win32' or 'linux':
        return uuid.getnode()
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())
