# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import winreg

def read_registry_value(hkey, key, value_name):
    try:
        # Open the registry key
        registry_key = winreg.OpenKey(hkey, key, 0, winreg.KEY_READ)

        # Read the value
        value, value_type = winreg.QueryValueEx(registry_key, value_name)

        # Close the registry key
        winreg.CloseKey(registry_key)

        return value
    except:
        return None
