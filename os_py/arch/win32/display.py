import win32api


def display_device():
    return win32api.EnumDisplayDevices().DeviceString


def screen_resolution():
    return f'{win32api.GetSystemMetrics(0)}x{win32api.GetSystemMetrics(1)}'


def screen_refresh_frequency():
    settings = win32api.EnumDisplaySettings(win32api.EnumDisplayDevices().DeviceName, -1)
    for varName in ['DisplayFrequency']:
        return str(getattr(settings, varName)) + 'Hz'
