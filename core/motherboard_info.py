import subprocess
import sys
import uuid
from core.exception import *


def motherboard_model():
    if sys.platform == 'win32':
        model = subprocess.check_output('wmic baseboard get product').decode().split('\n')[1].strip()
        return model
    else:
        return unsupported_exception()


def motherboard_manufacturer():
    if sys.platform == 'win32':
        manufacturer = subprocess.check_output('wmic baseboard get Manufacturer').decode().split('\n')[1].strip()
        return manufacturer
    else:
        return unsupported_exception()


def motherboard_serial_number():
    if sys.platform == 'win32':
        serial_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        return serial_id
    else:
        return unsupported_exception()


def motherboard_version():
    if sys.platform == 'win32':
        version = subprocess.check_output('wmic baseboard get version').decode().split('\n')[1].strip()
        return version
    else:
        return unsupported_exception()


def motherboard_node():
    if sys.platform == 'win32':
        return uuid.getnode()
    else:
        return unsupported_exception()
