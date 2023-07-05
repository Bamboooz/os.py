# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.prompt.prompt import execute_command

FINDMNT_GET_DEVICE = "findmnt -Do TARGET"
FINDMNT_GET_FSTYPE = "findmnt -Do FSTYPE"


def devices() -> dict:
    usbs = execute_command(FINDMNT_GET_DEVICE, 1).splitlines()
    fstypes = execute_command(FINDMNT_GET_FSTYPE, 1).splitlines()

    f_devices = {}

    for index, (usb, fstype) in enumerate(zip(usbs, fstypes)):
        if usb.startswith('/media'):
            f_devices[len(f_devices)] = [usb, usb.split('/')[-1], fstype]

    return f_devices


def num_devices() -> int:
    return len(devices())
