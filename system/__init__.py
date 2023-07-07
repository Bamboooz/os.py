# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import locale
import platform as _platform

from common.load import import_by_os, WINDOWS, LINUX


USER_PERMISSION_ADMINISTRATOR = 1
USER_PERMISSION_NORMAL = 0


def name() -> str:
    """ 
    Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

    An empty string is returned if the value cannot be determined.
    """
    return _platform.system()


def hostname() -> str:
    """
    Returns the computer's network name (which may not be fully qualified)

    An empty string is returned if the value cannot be determined.
    """
    return _platform.node()


def version() -> str:
    """
    Returns the system's release version, e.g. '#3 on degas'

    An empty string is returned if the value cannot be determined.
    """
    return _platform.version()


def platform() -> str:
    """
    Returns a single string identifying the underlying platform with as much useful information as possible (but no more :).

    The output is intended to be human-readable rather than machine parseable. It may look different on different platforms and this is intended.
    """
    return _platform.platform()


def release() -> str:
    """
    Returns the system's release, e.g. '2.2.0' or 'NT'

    An empty string is returned if the value cannot be determined.
    """
    return _platform.release()


def architecture() -> str:
    """
    Returns the architecture of the running operating system.
    """
    return _platform.architecture()[0]


def user() -> tuple:
    """
    Returns the username of the current user and his privileges.
    """
    username = os.environ.get('USERNAME')

    is_admin = import_by_os({
        WINDOWS: 'system.arch.windows.sys',
        LINUX: 'system.arch.windows.sys'
    }, 'is_admin')

    return username, is_admin


def lang() -> tuple:
    """
    Returns the system preferred language code as well as preferred encoding standard in a tuple.
    """
    lang_code, _ = locale.getdefaultlocale()
    encoding = locale.getpreferredencoding()
    return lang_code, encoding
