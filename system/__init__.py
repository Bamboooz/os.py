# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import platform

from common.data import ospylib_data_format


def system_info() -> ospylib_data_format:
    """
    Returns a namedtuple-like object containing a variety of system information.

    :returns:
        - name: Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.
        - hostname: Returns the computer's network name (which may not be fully qualified)
        - version: Returns the system's release version, e.g. '#3 on degas'
        - platform: Returns a single string identifying the underlying platform with as much useful information as possible (but no more :).
        - release: Returns the system's release, e.g. '2.2.0' or 'NT'
        - arch: Returns the architecture of the running operating system. e.g. x86_64
        - user: Returns the username of the current user and his privileges as a tuple (<user>, <is_admin>)
        - lang: Returns the current system language and its preferred encoding system in a tuple (<lang>, <encoding>)
    """
    if platform.system() == "Windows":  # later replace with c extension get operating system function
        system_info_format = ospylib_data_format("system_info", ["name", "hostname", "version", "platform", "release", "arch", "user", "lang", "uptime", "safe_mode", "hvci"])
        return system_info_format(name=None, hostname=None, version=None, platform=None, release=None, arch=None, user=None, lang=None, uptime=None, safe_mode=None, hvci=None)

    system_info_format = ospylib_data_format("system_info", ["name", "hostname", "version", "platform", "release", "arch", "user", "lang", "uptime"])
    return system_info_format(name=None, hostname=None, version=None, platform=None, release=None, arch=None, user=None, lang=None, uptime=None)
