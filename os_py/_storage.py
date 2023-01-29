import os
import psutil
import platform

from collections import defaultdict
from scripts._common import Handler


def _default_letter():
    letter = defaultdict(lambda: Handler.exception("Unsupported platform"),
                         windows='C',
                         linux='/',
                         linux2='/')
    return letter[platform.system().lower()]


def drive_list():
    disk_info = []
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        disk_info.append({
            'device': part.device,
        })
    return disk_info


def get_total_space(drive_letter=_default_letter()):
    if drive_letter != '/':
        drive_letter = drive_letter + ':\\'

    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.total / (1024.0 ** 3))) + 'GB'


def get_used_space(drive_letter=_default_letter()):
    if drive_letter != '/':
        drive_letter = drive_letter + ':\\'

    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.used / (1024.0 ** 3))) + 'GB'


def get_free_space(drive_letter=_default_letter()):
    if drive_letter != '/':
        drive_letter = drive_letter + ':\\'

    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.free / (1024.0 ** 3))) + 'GB'


def get_used_space_percent(drive_letter=_default_letter()):
    if drive_letter != '/':
        drive_letter = drive_letter + ':\\'

    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.percent)) + '%'
