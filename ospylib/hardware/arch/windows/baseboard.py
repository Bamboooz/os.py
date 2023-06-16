# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import winreg

from ospylib.common.registry import read_registry_value
from ospylib.common.prompt import execute_command

WMIC_PRODUCT = "wmic baseboard get product"
WMIC_MANUFACTURER = "wmic baseboard get manufacturer"
WMIC_VERSION = "wmic baseboard get version"

POWERSHELL_PRODUCT = "powershell.exe -Command \"Get-WmiObject Win32_BaseBoard | Select-Object Product\""
POWERSHELL_MANUFACTURER = "powershell.exe -Command \"Get-WmiObject Win32_BaseBoard | Select-Object Manufacturer"
POWERSHELL_VERSION = "powershell.exe -Command \"Get-WmiObject Win32_BaseBoard | Select-Object Version\""


class registry:
    @staticmethod
    def product() -> str:
        product = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardProduct").strip()
        return product

    @staticmethod
    def manufacturer() -> str:
        manufacturer = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardManufacturer").strip()
        return manufacturer

    @staticmethod
    def version() -> str:
        version = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardVersion").strip()
        return version


class wmic:
    @staticmethod
    def product() -> str:
        product = execute_command(WMIC_PRODUCT, 1).strip()
        return product

    @staticmethod
    def manufacturer() -> str:
        manufacturer = execute_command(WMIC_MANUFACTURER, 1).strip()
        return manufacturer

    @staticmethod
    def version() -> str:
        version = execute_command(WMIC_VERSION, 1).strip()
        return version


class powershell:
    @staticmethod
    def product() -> str:
        product = execute_command(POWERSHELL_PRODUCT, 3).strip()
        return product
    
    @staticmethod
    def manufacturer() -> str:
        manufacturer = execute_command(POWERSHELL_MANUFACTURER, 3).strip()
        return manufacturer
    
    @staticmethod
    def version() -> str:
        version = execute_command(POWERSHELL_VERSION, 3).strip()
        return version
