# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.prompt.prompt import execute_command

FINDMNT_GET_DEVICE = "findmnt -Do TARGET"
FINDMNT_GET_FSTYPE = "findmnt -Do FSTYPE"


def devices() -> list:
    usbs = execute_command(FINDMNT_GET_DEVICE, 1)
    return [usb for usb in usbs if usb.startswith("/media")]


def device_name(device) -> str:
    return device.split("/")[-1]


def device_fstype(device, devs) -> str:
    fstypes = execute_command(FINDMNT_GET_FSTYPE, 1)
    return {device: fstype for device, fstype in zip(devs, fstypes)}[device]
