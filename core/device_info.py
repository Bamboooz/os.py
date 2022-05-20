import os
import sys
import win32com.client
from core.exception import *


def get_usb_list():
    if sys.platform == 'win32':
        wmi = win32com.client.GetObject("winmgmts:")
        for usb in wmi.InstancesOf("Win32_USBHub"):
            return usb.DeviceID
    elif sys.platform == 'darwin':
        return
    elif sys.platform == 'linux':
        return os.popen('lsusb').read()
    else:
        return unsupported_exception()
