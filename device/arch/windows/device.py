# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import wmi

from common.path import drive_to_path as _dtp


def devices() -> dict:
    logical_disks = {
        _dtp(disk.DeviceID): [disk.VolumeName, disk.FileSystem]
        for num, disk in enumerate(wmi.WMI().Win32_LogicalDisk(DriveType=2))
    }

    return logical_disks
