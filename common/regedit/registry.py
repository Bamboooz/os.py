# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import winreg


def read_registry_value(hkey, key, value_name):
    registry_key = winreg.OpenKey(hkey, key, 0, winreg.KEY_READ)
    value, _ = winreg.QueryValueEx(registry_key, value_name)
    winreg.CloseKey(registry_key)
    return value
