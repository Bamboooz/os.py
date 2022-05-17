import sys
import win32com.client
from core.exception import *


def get_usb_list():
    if sys.platform == 'win32':
        wmi = win32com.client.GetObject("winmgmts:")
        for usb in wmi.InstancesOf("Win32_USBHub"):
            print(usb.DeviceID)
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()
