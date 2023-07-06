# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.load import import_by_os, WINDOWS, LINUX


devices = import_by_os({
    WINDOWS: 'device.arch.windows.device',
    LINUX: 'device.arch.windows.device'
}, 'devices')


num_devices = import_by_os({
    WINDOWS: 'device.arch.windows.device',
    LINUX: 'device.arch.windows.device'
}, 'num_devices')
