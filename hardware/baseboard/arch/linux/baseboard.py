# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

def product() -> str:
    with open("/sys/class/dmi/id/board_name", "r") as file:
        return file.read().strip()


def manufacturer() -> str:
    with open("/sys/class/dmi/id/board_vendor", "r") as file:
        return file.read().strip()
        

def version() -> str:
    with open("/sys/class/dmi/id/board_version", "r") as file:
        return file.read().strip()
