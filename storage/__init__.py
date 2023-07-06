# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import shutil
import system

from collections import namedtuple

from common.load import import_by_os, WINDOWS, LINUX
from common.path import drive_to_path as _dtp


drives: list = import_by_os({
    WINDOWS: 'storage.arch.windows.storage',
    LINUX: 'storage.arch.linux.storage'
}, 'drives')


def disk_usage(drive) -> namedtuple:
    disk_stat_format = namedtuple('disk_stat_format', ['total', 'used', 'free', 'perc_free', 'perc_used', 'filesystem'])

    if system.name() == 'Windows':
        drive = _dtp(drive)

    if not os.path.exists(drive) or os.path.isfile(drive):
        disk_stat = disk_stat_format(total=None, used=None, free=None, perc_free=None, perc_used=None, filesystem=None)
        return disk_stat

    total, used, free = shutil.disk_usage(drive)
    perc_free = free / total * 100
    perc_used = used / total * 100

    _filesystem = import_by_os({
        WINDOWS: 'storage.arch.windows.storage',
        LINUX: 'storage.arch.linux.storage'
    }, 'filesystem')

    disk_stat = disk_stat_format(total=total, used=used, free=free, perc_free=perc_free, perc_used=perc_used, filesystem=_filesystem(drive))
    return disk_stat
