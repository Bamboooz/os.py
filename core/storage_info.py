import os
import sys
import psutil
from core.exception import *


def drive_list():
    if sys.platform == 'win32':
        disk_info = []
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            disk_info.append({
                'device': part.device,
            })
        return disk_info
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif not sys.platform == 'linux':
        print(unsupported_func())
    else:
        print(unsupported_exception())


def get_total_space(drive_letter=None):
    if sys.platform == 'win32':
        if drive_letter is None:
            drive_letter = 'C'

        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            if part.device.startswith(drive_letter):
                return str(round(usage.total / 1024 ** 3)) + 'GB'
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        obj_disk = psutil.disk_usage('/')
        return str(round(obj_disk.total / (1024.0 ** 3))) + 'GB'
    else:
        print(unsupported_exception())


def get_used_space(drive_letter=None):
    if sys.platform == 'win32':
        if drive_letter is None:
            drive_letter = 'C'

        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            if part.device.startswith(drive_letter):
                return str(round(usage.used / 1024 ** 3)) + 'GB'
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        obj_disk = psutil.disk_usage('/')
        return str(round(obj_disk.used / (1024.0 ** 3))) + 'GB'
    else:
        print(unsupported_exception())


def get_free_space(drive_letter=None):
    if sys.platform == 'win32':
        if drive_letter is None:
            drive_letter = 'C'

        return str(int(get_total_space(drive_letter).replace('GB', '')) - int(get_used_space(drive_letter).replace('GB', ''))) + 'GB'
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        obj_disk = psutil.disk_usage('/')
        return str(round(obj_disk.free / (1024.0 ** 3))) + 'GB'
    else:
        print(unsupported_exception())


def get_used_space_percent(drive_letter=None):
    if sys.platform == 'win32':
        if drive_letter is None:
            drive_letter = 'C'

        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            if part.device.startswith(drive_letter):
                return str(usage.percent) + '%'
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        obj_disk = psutil.disk_usage('/')
        return str(round(obj_disk.percent)) + '%'
    else:
        print(unsupported_exception())


def get_drive_fstype(drive_letter=None):
    if sys.platform == 'win32':
        if drive_letter is None:
            drive_letter = 'C'

        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            if part.device.startswith(drive_letter):
                return part.fstype
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        print(unsupported_func())
    else:
        print(unsupported_exception())


def get_drive_mountpoint(drive_letter=None):
    if sys.platform == 'win32':
        if drive_letter is None:
            drive_letter = 'C'

        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            if part.device.startswith(drive_letter):
                return part.mountpoint
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        print(unsupported_func())
    else:
        print(unsupported_exception())
