# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess


def drives() -> list:
    return [f"/{mountpoint}" for mountpoint in os.listdir('/') if os.path.isdir(f'/{mountpoint}')]


def filesystem(mount_point):
    try:
        result = subprocess.run(['df', '-T', f'{mount_point}'], capture_output=True, text=True)
        return result.stdout.strip().splitlines()[1].split()[1] # The location filesystem is located in.
    except Exception:
        return None
