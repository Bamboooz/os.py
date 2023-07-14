# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


from collections import namedtuple

from common.load import import_by_os, WINDOWS, LINUX


def firmware_info() -> namedtuple:
    firmware_info_format = namedtuple('firmware_info_format', ['type', 'version', 'release_date', 'vendor'])

    firmware_type = None  # will implement when I will connect my C code with Python

    version = import_by_os({
        WINDOWS: "arch.windows.firmware",
        LINUX: "arch.linux.firmware"
    }, 'version')()

    release_date = import_by_os({
        WINDOWS: "arch.windows.firmware",
        LINUX: "arch.linux.firmware"
    }, 'release_date')()

    vendor = import_by_os({
        WINDOWS: "arch.windows.firmware",
        LINUX: "arch.linux.firmware"
    }, 'vendor')()

    return firmware_info_format(type=firmware_type, version=version, release_date=release_date, vendor=vendor)
