# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import ctypes
import re
import winreg

from ospy import toolbox

# Windows Registry key for firmware boot device
WINREG_FIRMWARE = [winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control", "FirmwareBootDevice"]


def winreg_get_firmware_type():
    """Determines the firmware type (BIOS or UEFI) using the Windows Registry."""
    firmware_type = toolbox.load_winreg_key(WINREG_FIRMWARE)

    # Check if the value is set to \EFI, which indicates UEFI
    if firmware_type == r"\EFI":
        return 'UEFI'
    else:
        return 'BIOS'


def ctypes_kernel32_get_firmware_type():
    """Determines the firmware type (BIOS or UEFI) using ctypes and the kernel32.dll."""
    firmware_type = None

    # Load the kernel32.dll library
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

    # Allocate a buffer for the firmware info
    buf_size = 1024
    firmware_info = ctypes.create_string_buffer(buf_size)

    # Call the GetFirmwareEnvironmentVariableW function to get the FirmwareType value
    status = kernel32.GetFirmwareEnvironmentVariableW(
        ctypes.c_wchar_p('FirmwareType').value,
        ctypes.c_wchar_p('{00000000-0000-0000-0000-000000000000}').value,
        firmware_info,
        buf_size
    )

    # Check the return value of the function call
    if status != 0:
        firmware_type = firmware_info.raw.decode().rstrip('\x00')
    elif ctypes.get_last_error() == 0x7a:  # ERROR_INVALID_PARAMETER
        firmware_type = 'BIOS'

    return firmware_type


def setupact_get_firmware_type():
    """Parses the setupact.log file to determine the firmware type (BIOS or UEFI)."""
    with open(r'C:\Windows\Panther\setupact.log') as f:
        pattern = re.compile(r'Detected boot environment: (\w+)')

        for line in f:
            match = pattern.search(line)
            if match:
                return match.group(1).upper()


def powershell_get_firmware_type():
    """
    Uses PowerShell to determine the firmware type (BIOS or UEFI).
    Call the read_powershell_command() function from the wintools module to execute a PowerShell command
    """
    output = toolbox.read_powershell_command("(Get-WmiObject -Class Win32_ComputerSystem).BootupState")[1]['output'].lower()

    if 'normal' in output:  # Check if the output contains "normal", which indicates BIOS
        return 'BIOS'
    elif 'uefi' in output or 'efi' in output:  # Check if the output contains "uefi" or "efi", which indicates UEFI
        return 'UEFI'
