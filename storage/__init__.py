# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import shutil

from common.path import drive_to_path as _dtp
from common.load import import_by_os, WINDOWS, LINUX


drives: list = import_by_os({
    WINDOWS: 'storage.arch.windows.storage',
    LINUX: 'storage.arch.linux.storage'
}, 'drives')


def s_total(drive) -> float:
    total = shutil.disk_usage(_dtp(drive))[0]
    return total


def s_used(drive) -> float:
    used = shutil.disk_usage(_dtp(drive))[1]
    return used


def s_free(drive) -> float:
    free = shutil.disk_usage(_dtp(drive))[2]
    return free


def p_free(drive) -> float:
    perc_free = s_free(_dtp(drive)) / s_total(_dtp(drive))
    return perc_free * 100


def p_used(drive) -> float:
    perc_used = s_used(_dtp(drive)) / s_total(_dtp(drive))
    return perc_used * 100
