# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import shutil
import string
import ctypes

# Define GB as a constant
GB = 1024 * 1024 * 1024


def _select_drive_list_method():
    """
    Try two different methods to get all available drives.
    Return a list of drive letters on success, none on failure.
    """
    try:
        return os_path_drive_list()
    except:
        try:
            return ctypes_windll_drive_list()
        except:
            return None


def os_path_drive_list():
    """
    Use os.path method to get all available drives.
    Return a list of drive letters on success.
    """
    return [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]


def ctypes_windll_drive_list():
    """
    Use ctypes.windll method to get all available drives.
    Return a list of drive letters on success.
    """
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()

    for i in range(26):
        if (bitmask >> i) & 1:
            drive = chr(i + 65) + ':\\'
            drive_type = ctypes.windll.kernel32.GetDriveTypeW(drive)
            if drive_type == 3:  # DRIVE_FIXED
                drives.append(drive)

    return drives


def _shutil_disk_data(mode, drive_letter=''):
    """
    Get disk usage for a given drive letter or for all available drives using shutil.
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    drives = [drive_letter] if drive_letter != '' else _select_drive_list_method()

    data = []

    for drive in drives:
        total, used, free = shutil.disk_usage(drive)
        data.append({
            'total': round(total / GB, 2),
            'used': round(used / GB, 2),
            'free': round(free / GB, 2),
            'used_percent': round(used / total * 100.0, 2)
        }.get(mode))

    return data[0] if len(data) == 1 else data


def _ctypes_windll_disk_data(mode, drive_letter=''):
    """
    Retrieves disk space information for the specified drive or all drives on the system, using ctypes.windll
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    drives = [drive_letter] if drive_letter != '' else _select_drive_list_method()
    data = []

    for drive in drives:
        free_bytes_available = ctypes.c_ulonglong(0)
        total_number_of_bytes = ctypes.c_ulonglong(0)
        total_number_of_free_bytes = ctypes.c_ulonglong(0)

        ret = ctypes.windll.kernel32.GetDiskFreeSpaceExW(
            ctypes.c_wchar_p(drive),
            ctypes.pointer(free_bytes_available),
            ctypes.pointer(total_number_of_bytes),
            ctypes.pointer(total_number_of_free_bytes))

        if ret == 0: raise Exception()

        data.append({
            "total": total_number_of_bytes.value / GB,
            "free": free_bytes_available.value / GB,
            "used": (total_number_of_bytes.value - free_bytes_available.value) / GB,
            "used_percent": (total_number_of_bytes.value - free_bytes_available.value) / total_number_of_bytes.value * 100.0
        }.get(mode))

    return data[0] if len(data) == 1 else data


def shutil_disk_total_space(drive_letter=''):
    """
    Get the total disk space in GB, using shutil, for a given drive letter or for all available drives.
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    return _shutil_disk_data('total', drive_letter)


def shutil_disk_used_space(drive_letter=''):
    """
    Get the used disk space in GB, using shutil, for a given drive letter or for all available drives.
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    return _shutil_disk_data('used', drive_letter)


def shutil_disk_free_space(drive_letter=''):
    """
    Get the free disk space in GB, using shutil, for a given drive letter or for all available drives.
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    return _shutil_disk_data('free', drive_letter)


def shutil_disk_used_space_percent(drive_letter=''):
    """
    Get the percentage of used disk space, using shutil, for a given drive letter or for all available drives.
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    return _shutil_disk_data('used_percent', drive_letter)


def ctypes_windll_get_total_space(drive_letter=''):
    """
    Get the total disk space, using ctypes.windll in GB, for a given drive letter or for all available drives.
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    return _ctypes_windll_disk_data('total', drive_letter)


def ctypes_windll_get_used_space(drive_letter=''):
    """
    Get the used disk space, using ctypes.windll in GB, for a given drive letter or for all available drives.
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    return _ctypes_windll_disk_data('used', drive_letter)


def ctypes_windll_get_free_space(drive_letter=''):
    """
    Get the free disk space, using ctypes.windll in GB, for a given drive letter or for all available drives.
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    return _ctypes_windll_disk_data('free', drive_letter)


def ctypes_windll_get_used_space_percent(drive_letter=''):
    """
    Get the percentage of used disk space, using ctypes.windll, for a given drive letter or for all available drives.
    Return a float if drive_letter is given, a list of floats otherwise.
    """
    return _ctypes_windll_disk_data('used_percent', drive_letter)
