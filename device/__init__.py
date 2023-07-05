# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.load import import_by_os, WINDOWS, LINUX


devices: dict = import_by_os({
    WINDOWS: 'windows',
    LINUX: 'linux'
}, 'devices')


num_devices: int = import_by_os({
    WINDOWS: 'windows',
    LINUX: 'linux'
}, 'num_devices')
