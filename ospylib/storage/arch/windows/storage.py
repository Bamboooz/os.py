# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import shutil
import string


def _g_root(drive) -> str:
    """
    Converts drive letters to root paths ("C" -> "C:\\", "C:\\" -> "C:\\") etc.
    """
    return (drive.strip().upper().rstrip("\\") + "\\") if len(drive.strip()) > 1 else drive.strip().upper() + ":\\"


def drives() -> list:
    return [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]


def s_total(drive) -> float:
    total = shutil.disk_usage(_g_root(drive))[0]
    return total


def s_used(drive) -> float:
    used = shutil.disk_usage(_g_root(drive))[1]
    return used


def s_free(drive) -> float:
    free = shutil.disk_usage(_g_root(drive))[2]
    return free


def p_free(drive) -> float:
    perc_free = s_free(_g_root(drive)) / s_total(_g_root(drive))
    return perc_free * 100


def p_used(drive) -> float:
    perc_used = s_used(_g_root(drive)) / s_total(_g_root(drive))
    return perc_used * 100
