# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import winreg

from common.regedit.registry import read_registry_value


def version() -> str:
    firmware_version = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\SystemInformation", "BIOSVersion").strip()
    return firmware_version


def release_date() -> str:
    firmware_release_date = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\SystemInformation", "BIOSReleaseDate").strip()
    return firmware_release_date


def vendor() -> str:
    firmware_vendor = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\DESCRIPTION\System\BIOS", "BIOSVendor").strip()
    return firmware_vendor
