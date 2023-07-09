# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import shutil
import device

from collections import namedtuple

from common.load import import_by_os, WINDOWS, LINUX
from common.path import drive_to_path as _dtp


drives = import_by_os({
    WINDOWS: 'storage.arch.windows.storage',
    LINUX: 'storage.arch.linux.storage'
}, 'drives')


def disk_usage(drive) -> namedtuple:
    disk_stat_format = namedtuple('disk_stat_format', ['total', 'used', 'free', 'perc_free', 'perc_used'])

    drive = _dtp(drive)

    is_mount = os.path.exists(drive) and drive.startswith("/") and not os.path.isfile(drive)
    is_drive = os.path.exists(drive) and os.path.isabs(drive) and len(os.path.splitdrive(drive)[0]) == 2 and not os.path.isfile(drive)

    if not is_mount and not is_drive:
        disk_stat = disk_stat_format(total=None, used=None, free=None, perc_free=None, perc_used=None)
        return disk_stat

    total, used, free = shutil.disk_usage(drive)
    perc_free = free / total * 100
    perc_used = used / total * 100

    disk_stat = disk_stat_format(total=total, used=used, free=free, perc_free=perc_free, perc_used=perc_used)
    return disk_stat


def disk_partitions(drive) -> namedtuple:
    disk_partitions_format = namedtuple('disk_partitions_format', ['fstype', 'type'])
    disk_type_format = namedtuple('disk_type_format', ['removable', 'drive', 'mount'])

    drive = _dtp(drive)

    is_mount = os.path.exists(drive) and drive.startswith("/") and not os.path.isfile(drive)
    is_drive = os.path.exists(drive) and os.path.isabs(drive) and len(os.path.splitdrive(drive)[0]) == 2 and not os.path.isfile(drive)
    is_removable = drive in device.ext_dev()

    if not is_mount and not is_drive:
        disk_type = disk_type_format(removable=None, drive=None, mount=None)
        disk_stat = disk_partitions_format(fstype=None, type=disk_type)
        return disk_stat

    filesystem = import_by_os({
        WINDOWS: 'storage.arch.windows.storage',
        LINUX: 'storage.arch.linux.storage'
    }, 'filesystem')(drive)

    disk_type = disk_type_format(drive=is_drive, mount=is_mount, removable=is_removable)
    partitions = disk_partitions_format(fstype=filesystem, type=disk_type)
    return partitions
