# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import shutil
import device

from common.load import import_by_os
from common.fs.path import drive_to_path as _dtp
from common.data import ospylib_data_format


def drives() -> list:
    """
    Get a list of all available installed drives.
    """
    drive_list = import_by_os(windows="storage.arch.windows.storage", linux="storage.arch.linux.storage", function="drives")
    return drive_list()


def disk_usage(drive) -> ospylib_data_format:
    """
    Returns a namedtuple-like containing information about specified drive's usages.

    :returns:
        - total: Returns the total amount of drive space in bytes.
        - used: Returns the used amount of drive space in bytes.
        - free: Returns the free amount of drive space in bytes.
        - perc_free: Returns the free amount of drive space in percentage.
        - perc_used: Returns the used amount of drive space in percentage.
    """
    drive = _dtp(drive)

    is_mount = os.path.exists(drive) and drive.startswith("/") and not os.path.isfile(drive)
    is_drive = os.path.exists(drive) and os.path.isabs(drive) and len(os.path.splitdrive(drive)[0]) == 2 and not os.path.isfile(drive)

    if not is_mount and not is_drive:
        return ospylib_data_format(total=None, used=None, free=None, perc_free=None, perc_used=None)

    total, used, free = shutil.disk_usage(drive)
    perc_free = free / total * 100
    perc_used = used / total * 100

    return ospylib_data_format(total=total, used=used, free=free, perc_free=perc_free, perc_used=perc_used)


def disk_info(drive) -> ospylib_data_format:
    """
    Returns a namedtuple-like object containing information about selected drive.

    :returns:
        - fstype: Returns the filesystem type of the requested drive
        - type:
            - drive: Returns if the selected disk is a drive
            - mount: Returns if the selected disk is a mount
            - removable: Returns if the selected disk is a removable disk device
    """
    drive = _dtp(drive)

    is_mount = os.path.exists(drive) and drive.startswith("/") and not os.path.isfile(drive)
    is_drive = os.path.exists(drive) and os.path.isabs(drive) and len(os.path.splitdrive(drive)[0]) == 2 and not os.path.isfile(drive)

    if not is_mount and not is_drive:
        disk_type = ospylib_data_format(removable=None, drive=None, mount=None)
        return ospylib_data_format(fstype=None, type=disk_type)

    disk_type = ospylib_data_format(drive=is_drive, mount=is_mount, removable=[_is_removable, [drive]])

    return ospylib_data_format(fstype=[_get_fst, [drive]], type=disk_type)


def _is_removable(drive) -> bool:
    """
    Check if requested drive is removable.
    """
    return drive in device.ext_dev()


def _get_fst(drive) -> str:
    """
    Get filesystem of a requested drive.
    """
    filesystem = import_by_os(windows="storage.arch.windows.storage", linux="storage.arch.linux.storage", function="filesystem")
    return filesystem(drive)
