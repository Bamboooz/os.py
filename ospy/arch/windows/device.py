# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from ospy import toolbox


def wmic_get_number_of_external_drives():
    """
    Returns the number of external drives connected to the computer,
    using the WMIC command to query the system for logical disks with a drivetype of 2 (which corresponds to removable drives).

    Returns:
        Number of external devices connected to the machine
    """
    return len(toolbox.parse_wmic('wmic logicaldisk where drivetype=2 get DeviceID, VolumeName, Description'))


def wmic_get_external_drives():
    """
    Returns a list of external drives connected to the computer,
    using the WMIC command to query the system for logical disks with a drivetype of 2 (which corresponds to removable drives).
    """
    output = toolbox.parse_wmic("wmic logicaldisk where drivetype=2 get DeviceID")

    return [v['output'].strip() for k, v in output.items()]


def powershell_get_number_of_external_drives():
    """
    Returns the number of external drives connected to the computer,
    using a PowerShell command to query the system for logical disks with a drivetype of 2 (which corresponds to removable drives).
    """
    devices = toolbox.read_powershell_command('Get-WmiObject Win32_LogicalDisk | Where-Object {$_.DriveType -eq 2} | Select-Object -ExpandProperty DeviceID')

    if devices is None: return 0

    return len(devices)


def powershell_get_external_drives():
    """
    Returns a list of external drives connected to the computer,
    using a PowerShell command to query the system for logical disks with a drivetype of 2 (which corresponds to removable drives).
    """
    devices = toolbox.read_powershell_command('Get-WmiObject Win32_LogicalDisk | Where-Object {$_.DriveType -eq 2} | Select-Object -ExpandProperty DeviceID')

    if devices is None: return []

    return [v['output'].strip() for k, v in devices.items()]
