import os
import sys
import psutil

from scripts.err import Errors


def default_letter():
    return {
        'windows': "C",
        'linux' or 'linux2': '/'
    }.get(sys.platform.lower(), Errors().unsupported_os())


def drive_list():  # win32 only
    disk_info = []
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        disk_info.append({
            'device': part.device,
        })
    return disk_info


def get_total_space(drive_letter=default_letter()):
    if drive_letter is not '/':
        drive_letter = drive_letter + ':\\'

    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.total / (1024.0 ** 3))) + 'GB'


def get_used_space(drive_letter=default_letter()):
    if drive_letter is not '/':
        drive_letter = drive_letter + ':\\'

    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.used / (1024.0 ** 3))) + 'GB'


def get_free_space(drive_letter=default_letter()):
    if drive_letter is not '/':
        drive_letter = drive_letter + ':\\'

    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.free / (1024.0 ** 3))) + 'GB'


def get_used_space_percent(drive_letter=default_letter()):
    if drive_letter is not '/':
        drive_letter = drive_letter + ':\\'

    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.percent)) + '%'
