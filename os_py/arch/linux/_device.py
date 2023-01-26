import os


def get_usb_list():
    return os.popen('lsusb').read()

