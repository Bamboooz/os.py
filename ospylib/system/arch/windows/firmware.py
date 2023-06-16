# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import winreg
import ctypes

from ospylib.common.registry import read_registry_value


def firmware() -> str:
    """
    Detects user firmware type, which is BIOS or UEFI.
    """
    firmware_info = ctypes.create_string_buffer(512)
    result = ctypes.windll.kernel32.GetFirmwareEnvironmentVariableA(b"SecureBoot", b"{00000000-0000-0000-0000-000000000000}", firmware_info, ctypes.sizeof(firmware_info))
    return 'UEFI' if result > 0 else 'BIOS'


class registry:
    @staticmethod
    def firmware() -> str:
        s_firmware = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\SecureBoot\\State", "UEFISecureBootEnabled")
        return "UEFI" if s_firmware == 1 else "BIOS"

    @staticmethod
    def vendor() -> str:
        s_vendor = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BIOSVendor")
        return s_vendor

    @staticmethod
    def version() -> str:
        s_version = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BIOSVersion")
        return s_version
