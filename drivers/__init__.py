# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.load import import_by_os, WINDOWS, LINUX


get_drivers: dict = import_by_os({
    WINDOWS: 'drivers.arch.windows.drivers',
    LINUX: 'drivers.arch.linux.drivers'
}, 'get_drivers')
