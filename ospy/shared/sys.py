# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import platform


def os_name():
    """
    Returns the name of the operating system.
    """
    return platform.system()


def machine_hostname():
    """
    Returns the hostname of the machine.
    """
    return platform.node()


def os_version():
    """
    Returns the version of the operating system.
    """
    return platform.version()


def os_platform():
    """
    Returns the platform of the operating system.
    """
    return platform.platform()


def os_release():
    """
    Returns the release of the operating system.
    """
    return platform.release()


def os_architecture():
    """
    Returns the architecture of the operating system.
    """
    return platform.architecture()[0]
