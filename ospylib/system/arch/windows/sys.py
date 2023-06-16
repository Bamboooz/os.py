# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import ctypes
import winreg
import platform as _platform


USER_PERMISSION_ADMINISTRATOR = 1
USER_PERMISSION_NORMAL = 0


def name() -> str:
    """
    Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Darwin'.

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


def user() -> list:
    """
    Returns the username of the current user.
    """
    username = os.environ.get('USERNAME')
    privileges = ctypes.windll.shell32.IsUserAnAdmin()
    return [username, USER_PERMISSION_ADMINISTRATOR if privileges == 1 else USER_PERMISSION_NORMAL]


def users() -> dict:
    """
    Gets a dictionary containing all users on a system and corresponding to them privileges.
    """
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList")

    return {
        i: [winreg.QueryValueEx(winreg.OpenKey(reg_key, sid), "ProfileImagePath")[0].split("\\")[-1],
            USER_PERMISSION_ADMINISTRATOR if ctypes.windll.shell32.IsUserAnAdmin(sid) else USER_PERMISSION_NORMAL]
        for i, sid in enumerate([winreg.EnumKey(reg_key, j) for j in range(winreg.QueryInfoKey(reg_key)[0])])
    }


def uptime() -> int:
    """
    Returns operating system uptime in seconds.
    """
    return ctypes.windll.kernel32.GetTickCount() // 1000


def safe_mode() -> bool:
    """
    Detects if the code was run on a system booted in safe mode.
    """
    return ctypes.WinDLL("user32").GetSystemMetrics(67) != 0


def hvci():
    """
    Detects if system was run using HVCI hypervisor.
    """
    return bool(ctypes.c_ulong().value & 0x20)
