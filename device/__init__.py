# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.data import ospylib_data_format
from common.load import import_by_os, WINDOWS, LINUX
from common.path import drive_to_path as _dtp


def ext_dev(device: str=None) -> ospylib_data_format or list:
    ext_dev_format = namedtuple('ext_dev_format', ['name', 'fstype'])

    device_data = import_by_os({
        WINDOWS: 'device.arch.windows.device',
        LINUX: 'device.arch.windows.device'
    }, 'devices')()

    devices = list(device_data.keys())

    if device is None:
        return devices

    device = _dtp(device)

    if device in devices:
        name = device_data[device][0]
        fstype = device_data[device][1]
        return ext_dev_format(name=name, fstype=fstype)


    return ext_dev_format(name=None, fstype=None)
