# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.data import ospylib_data_format
from common.load import import_by_os


def driver_query() -> ospylib_data_format:
    """
    Returns a namedtuple-like object containing a variety of system information.

    :returns:
        - name: Operating system e.g. Windows, Linux
        - hostname: Returns the computer's network name (which may not be fully qualified)
        - version: Returns the system's release version, e.g. '#3 on degas'
        - platform: Returns a single string identifying the underlying platform with as much useful information as possible (but no more :).
        - release: Returns the system's release, e.g. '2.2.0' or 'NT'
        - arch: Returns the architecture of the running operating system. e.g. x86_64
        - user: Returns the username of the current user and his privileges as a tuple (<user>, <is_admin>)
        - lang: Returns the current system language and its preferred encoding system in a tuple (<lang>, <encoding>)
    """
    driver_query_function = import_by_os(windows="drivers.arch.windows.drivers", linux="drivers.arch.linux.drivers", function="driver_query")
    return driver_query_function()
