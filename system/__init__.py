# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import locale
import platform as platform

from collections import namedtuple


def system_info() -> namedtuple:
    """
    Returns a namedtuple containing a variety of system information.

    Returns a named tuple containing:
        - name: Operating system e.g. Windows, Linux
        - hostname: Returns the computer's network name (which may not be fully qualified)
        - version: Returns the system's release version, e.g. '#3 on degas'
        - platform: Returns a single string identifying the underlying platform with as much useful information as possible (but no more :).
        - release: Returns the system's release, e.g. '2.2.0' or 'NT'
        - arch: Returns the architecture of the running operating system. e.g. x86_64
        - user: Returns the username of the current user and his privileges as a tuple (<user>, <is_admin>)
        - lang: Returns the current system language and its preferred encoding system in a tuple (<lang>, <encoding>)
    """
    system_name = _name()

    if system_name == 'Windows':
        system_info_format = namedtuple('system_info_format', ['name', 'hostname', 'version', 'platform', 'release', 'arch', 'user', 'lang', 'uptime', 'is_admin', 'safe_mode', 'hvci'])
        return system_info_format(name=system_name, hostname=_hostname(), version=_version(), platform=_platform(), release=_release(), arch=_architecture(), user=_user(), lang=_lang(), uptime=None, is_admin=None, safe_mode=None, hvci=None)

    system_info_format = namedtuple('system_info_format', ['name', 'hostname', 'version', 'platform', 'release', 'arch', 'user', 'lang', 'uptime', 'is_admin'])
    return system_info_format(name=system_name, hostname=_hostname(), version=_version(), platform=_platform(), release=_release(), arch=_architecture(), user=_user(), lang=_lang(), uptime=None, is_admin=None)


def _name() -> str:
    """ 
    Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

    An empty string is returned if the value cannot be determined.
    """
    return platform.system()


def _hostname() -> str:
    """
    Returns the computer's network name (which may not be fully qualified)

    An empty string is returned if the value cannot be determined.
    """
    return platform.node()


def _version() -> str:
    """
    Returns the system's release version, e.g. '#3 on degas'

    An empty string is returned if the value cannot be determined.
    """
    return platform.version()


def _platform() -> str:
    """
    Returns a single string identifying the underlying platform with as much useful information as possible (but no more :).

    The output is intended to be human-readable rather than machine parseable. It may look different on different platforms and this is intended.
    """
    return platform.platform()


def _release() -> str:
    """
    Returns the system's release, e.g. '2.2.0' or 'NT'

    An empty string is returned if the value cannot be determined.
    """
    return platform.release()


def _architecture() -> str:
    """
    Returns the architecture of the running operating system.
    """
    return platform.architecture()[0]


def _user() -> tuple:
    """
    Returns the username of the current user and his privileges.
    """
    username = os.environ.get('USERNAME')

    is_admin = None  # ospylib C extensions not yet connected with the Python code.

    return username, is_admin


def _lang() -> tuple:
    """
    Returns the system preferred language code as well as preferred encoding standard in a tuple.
    """
    lang_code, _ = locale.getdefaultlocale()
    encoding = locale.getpreferredencoding()
    return lang_code, encoding
