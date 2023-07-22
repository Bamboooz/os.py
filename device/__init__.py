# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import platform

from common.data import ospylib_data_format
from common.load import import_by_os
from common.fs.path import drive_to_path as _dtp


def ext_dev(device=None) -> ospylib_data_format or list:
    devices = import_by_os(windows="device.arch.windows.device", linux="device.arch.linux.device", function="devices")()

    if device is None:
        return devices

    device = _dtp(device)

    if device not in devices:
        return ospylib_data_format(name=None, fstype=None)

    name = import_by_os(windows="device.arch.windows.device", linux="device.arch.linux.device", function="device_name")
    fstype = import_by_os(windows="device.arch.windows.device", linux="device.arch.linux.device", function="device_fstype")

    if platform.system() == 'Windows':
        return ospylib_data_format(name=[name, [device, devices]], fstype=[fstype, [device, devices]])

    return ospylib_data_format(name=[name, [device]], fstype=[fstype, [device, devices]])
