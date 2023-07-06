# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.load import import_by_os, WINDOWS, LINUX


class baseboard:
    product = import_by_os({
        WINDOWS: 'hardware.arch.windows.baseboard',
        LINUX: 'hardware.arch.linux.baseboard'
    }, 'product')

    manufacturer = import_by_os({
        WINDOWS: 'hardware.arch.windows.baseboard',
        LINUX: 'hardware.arch.linux.baseboard'
    }, 'manufacturer')

    version = import_by_os({
        WINDOWS: 'hardware.arch.windows.baseboard',
        LINUX: 'hardware.arch.linux.baseboard'
    }, 'version')
