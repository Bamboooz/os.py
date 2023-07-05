# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os


def drives() -> list:
    return [mountpoint for mountpoint in os.listdir('/') if os.path.isdir(f'/{mountpoint}')]
