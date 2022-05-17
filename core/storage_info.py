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
    else:
        return unsupported_exception()


def get_total_space(drive_letter):
    if sys.platform == 'win32':
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            if part.device.startswith(drive_letter):
                return str(round(usage.total / 1024 ** 3)) + 'GB'
    else:
        return unsupported_exception()


def get_used_space(drive_letter):
    if sys.platform == 'win32':
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            if part.device.startswith(drive_letter):
                return str(round(usage.used / 1024 ** 3)) + 'GB'
    else:
        return unsupported_exception()


def get_free_space(drive_letter):
    return str(int(get_total_space(drive_letter).replace('GB', '')) - int(get_used_space(drive_letter).replace('GB', ''))) + 'GB'


def get_used_space_percent(drive_letter):
    if sys.platform == 'win32':
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            if part.device.startswith(drive_letter):
                return str(usage.percent) + '%'
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
