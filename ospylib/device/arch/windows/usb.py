# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from ospylib.common.prompt import execute_command
from ospylib.storage.arch.windows.storage import *

WMIC_EXT_DEVICES = "wmic logicaldisk where drivetype=2 get DeviceID, VolumeName"

POWERSHELL_EXT_DEVICES = "powershell.exe -c \"Get-WmiObject -Class Win32_LogicalDisk | Where-Object { $_.DriveType -eq 2 } | Select-Object DeviceID, VolumeName\""


def d_root(drive) -> str:
    if not drive.endswith(":"):
        drive += ":"

    if not drive.endswith("\\"):
        drive += "\\"

    return drive


class wmic:
    @staticmethod
    def ext_devices() -> dict:
        devices = execute_command(WMIC_EXT_DEVICES, 1)

        ext_devices = {}

        for device, line in enumerate([item for item in devices.split('\n') if item != '']):
            ext_devices[device] = {
                'letter': d_root(line.split(' ')[0]),
                'name': "".join(line.split(' ')[1:]).strip(),
                'm_total': s_total(d_root(line.split(' ')[0])),
                'm_used': s_used(d_root(line.split(' ')[0])),
                'm_free': s_free(d_root(line.split(' ')[0])),
                'p_used': p_used(d_root(line.split(' ')[0])),
                'p_free': p_free(d_root(line.split(' ')[0]))
            }

        return ext_devices

    def num_ext_devices(self) -> int:
        external_devices = self.ext_devices()
        return len(external_devices) if external_devices != -1 else -1


class powershell:
    @staticmethod
    def ext_devices() -> dict:
        devices = execute_command(POWERSHELL_EXT_DEVICES, 3)

        ext_devices = {}

        for device, line in enumerate([item for item in devices.split('\n') if item != '']):
            ext_devices[device] = {
                'letter': d_root(line.split(' ')[0]),
                'name': "".join(line.split(' ')[1:]).strip(),
                'm_total': s_total(d_root(line.split(' ')[0])),
                'm_used': s_used(d_root(line.split(' ')[0])),
                'm_free': s_free(d_root(line.split(' ')[0])),
                'p_used': p_used(d_root(line.split(' ')[0])),
                'p_free': p_free(d_root(line.split(' ')[0]))
            }

        return ext_devices

    def num_ext_devices(self) -> int:
        external_devices = self.ext_devices()
        return len(external_devices) if external_devices != -1 else -1
