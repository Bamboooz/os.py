import win32com.client


def get_usb_list():
    wmi = win32com.client.GetObject("winmgmts:")
    for usb in wmi.InstancesOf("Win32_USBHub"):
        return usb.DeviceID
