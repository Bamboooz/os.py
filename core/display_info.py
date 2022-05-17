import sys
from core.exception import unsupported_exception
import win32api
import ctypes


def display_device():
    if sys.platform == 'win32':
        return win32api.EnumDisplayDevices().DeviceName, win32api.EnumDisplayDevices().DeviceString
    else:
        return unsupported_exception()


def screen_resolution():
    if sys.platform == 'win32':
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    else:
        return unsupported_exception()


def screen_refresh_frequency():
    if sys.platform == 'win32':
        settings = win32api.EnumDisplaySettings(win32api.EnumDisplayDevices().DeviceName, -1)
        for varName in ['DisplayFrequency']:
            return str(getattr(settings, varName)) + 'Hz'
    else:
        return unsupported_exception()
