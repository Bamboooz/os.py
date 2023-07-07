# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import ctypes


def is_admin():
    # Return if current user is an administrator.
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
