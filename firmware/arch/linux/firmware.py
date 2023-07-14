# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


def version() -> str:
    with open("/sys/class/dmi/id/bios_version", 'r') as dmi_file:
        return dmi_file.read().strip()


def release_date() -> str:
    with open("/sys/class/dmi/id/bios_release", 'r') as dmi_file:
        return dmi_file.read().strip()


def vendor() -> str:
    with open("/sys/class/dmi/id/bios_vendor", 'r') as dmi_file:
        return dmi_file.read().strip()
