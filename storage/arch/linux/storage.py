# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os

from common.prompt.prompt import execute_command


def drives() -> list:
    return [mountpoint for mountpoint in os.listdir('/') if os.path.isdir(f'/{mountpoint}')]


def filesystem(mount_point):
    try:
        output = execute_command(f'df -T {mount_point}', trim=1)
        filesystem = output[0].split()[1]
        return filesystem
    except:
        return None
