import os
import sys
import psutil
import string
from core.exception import *


obj_Disk = psutil.disk_usage('/')


def drive_list():
    if sys.platform == 'win32':
        return ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    else:
        return unsupported_exception()


def get_total_space():
    if sys.platform == 'win32' or 'linux':
        return str(round(obj_Disk.total / (1024.0 ** 3))) + 'GB'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def get_used_space():
    if sys.platform == 'win32' or 'linux':
        return str(round(obj_Disk.used / (1024.0 ** 3))) + 'GB'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def get_free_space():
    if sys.platform == 'win32' or 'linux':
        return str(round(obj_Disk.free / (1024.0 ** 3))) + 'GB'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def get_used_space_percent():
    if sys.platform == 'win32' or 'linux':
        return str(obj_Disk.percent) + 'GB'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def get_drive_fstype(drive_letter):
    if sys.platform == 'win32':
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            if part.device.startswith(drive_letter):
                return part.fstype
    else:
        return unsupported_exception()


def get_drive_mountpoint(drive_letter):
    if sys.platform == 'win32':
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            if part.device.startswith(drive_letter):
                return part.mountpoint
    else:
        return unsupported_exception()
