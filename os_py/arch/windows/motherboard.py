# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import winreg

from os_py.arch.windows import wintools

# Define constants for WMIC commands
WMIC_PRODUCT = 'wmic baseboard get product'
WMIC_MANUFACTURER = 'wmic baseboard get manufacturer'
WMIC_VERSION = 'wmic baseboard get version'

# Define constants for WinReg keys
WINREG_BASEBOARD = [winreg.HKEY_LOCAL_MACHINE, r'HARDWARE\DESCRIPTION\System\BIOS', 'BaseBoardProduct']
WINREG_MANUFACTURER = [winreg.HKEY_LOCAL_MACHINE, r'HARDWARE\DESCRIPTION\System\BIOS', 'BaseBoardManufacturer']
WINREG_VERSION = [winreg.HKEY_LOCAL_MACHINE, r'HARDWARE\DESCRIPTION\System\BIOS', 'BaseBoardVersion']


def wmic_get_motherboard_product():
    """Uses WMIC to retrieve the motherboard product name."""
    return wintools.parse_wmic(WMIC_PRODUCT)[1]['output']


def wmic_get_motherboard_manufacturer():
    """Uses WMIC to retrieve the motherboard manufacturer name."""
    return wintools.parse_wmic(WMIC_MANUFACTURER)[1]['output']


def wmic_get_motherboard_version():
    """Uses WMIC to retrieve the motherboard version."""
    return wintools.parse_wmic(WMIC_VERSION)[1]['output']


def winreg_get_motherboard_product():
    """Uses WinReg to retrieve the motherboard product name."""
    return wintools.load_winreg_key(WINREG_BASEBOARD)


def winreg_get_motherboard_manufacturer():
    """Uses WinReg to retrieve the motherboard manufacturer name."""
    return wintools.load_winreg_key(WINREG_MANUFACTURER)


def winreg_get_motherboard_version():
    """Uses WinReg to retrieve the motherboard version."""
    return wintools.load_winreg_key(WINREG_VERSION)
