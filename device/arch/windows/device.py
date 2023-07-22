# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import wmi

from common.fs.path import drive_to_path as _dtp


def devices() -> list:
    return [_dtp(disk.DeviceID) for disk in wmi.WMI().Win32_LogicalDisk(DriveType=2)]


def device_name(device, devs) -> str:
    return dict(zip(devs, [disk.VolumeName for disk in wmi.WMI().Win32_LogicalDisk(DriveType=2)]))[device]


def device_fstype(device, devs) -> str:
    return dict(zip(devs, [disk.FileSystem for disk in wmi.WMI().Win32_LogicalDisk(DriveType=2)]))[device]
