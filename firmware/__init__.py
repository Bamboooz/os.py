# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.data import ospylib_data_format
from common.load import import_by_os


def firmware_info() -> ospylib_data_format:
    firmware_type = None  # will implement when I will connect my C code with Python

    version = import_by_os(windows="arch.windows.firmware", linux="arch.linux.firmware", function="version")
    release_date = import_by_os(windows="arch.windows.firmware", linux="arch.linux.firmware", function="release_date")
    vendor = import_by_os(windows="arch.windows.firmware", linux="arch.linux.firmware", function="vendor")

    return ospylib_data_format(type=firmware_type, version=version, release_date=release_date, vendor=vendor)
