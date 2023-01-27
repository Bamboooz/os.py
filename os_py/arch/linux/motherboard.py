import os
import uuid


def motherboard_model():
    return os.system('cat /sys/devices/virtual/dmi/id/board_name')


def motherboard_manufacturer():
    return os.system('cat /sys/devices/virtual/dmi/id/board_vendor')


def motherboard_serial_number():
    return os.system('cat /sys/class/dmi/id/board_serial')


def motherboard_version():
    return os.system('cat /sys/class/dmi/id/board_version:')


def motherboard_node():
    return uuid.getnode()
