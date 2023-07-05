# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import wmi
import winreg

from common.regedit.registry import read_registry_value
from common.load import load_method


class registry:
    @staticmethod
    def product() -> str:
        return read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardProduct").strip()

    @staticmethod
    def manufacturer() -> str:
        return read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardManufacturer").strip()

    @staticmethod
    def version() -> str:
        return read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardVersion").strip()


class wmic:
    @staticmethod
    def product() -> str:
        for baseboard in wmi.WMI().Win32_BaseBoard():
            return baseboard.Product

    @staticmethod
    def manufacturer() -> str:
        for baseboard in wmi.WMI().Win32_BaseBoard():
            return baseboard.Manufacturer

    @staticmethod
    def version() -> str:
        for baseboard in wmi.WMI().Win32_BaseBoard():
            return baseboard.Version


def product() -> str:
    return load_method([registry, wmic], 'product', None)


def manufacturer() -> str:
    return load_method([registry, wmic], 'manufacturer', None)


def version() -> str:
    return load_method([registry, wmic], 'version', None)
