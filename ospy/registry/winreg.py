# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import ctypes

HKEY_CLASSES_ROOT = 0x80000000
HKEY_CURRENT_USER = 0x80000001
HKEY_LOCAL_MACHINE = 0x80000002
HKEY_USERS = 0x80000003

KEY_READ = 0x20019
KEY_WRITE = 0x20006
KEY_READ_WRITE = KEY_WRITE | KEY_READ


def open_key(key_path, root_key=HKEY_LOCAL_MACHINE, access=KEY_READ):
    hkey = ctypes.c_void_p()
    result = ctypes.windll.advapi32.RegOpenKeyExA(
        root_key,
        key_path.encode('utf-8'),
        0,
        access,
        ctypes.byref(hkey)
    )
    if result != 0:
        raise WindowsError("Error opening registry key: {}".format(result))
    return hkey


def read_value(key, value_name):
    value_data = ctypes.create_string_buffer(1024)
    value_size = ctypes.c_ulong(1024)
    result = ctypes.windll.advapi32.RegQueryValueExA(
        key,
        value_name.encode('utf-8'),
        None,
        None,
        ctypes.cast(value_data, ctypes.c_void_p),
        ctypes.byref(value_size)
    )
    if result != 0:
        raise WindowsError("Error reading registry value: {}".format(result))
    return value_data.value.decode('utf-8')


def write_value(key, value_name, value_data, value_type=1):
    value_data = value_data.encode('utf-8')
    result = ctypes.windll.advapi32.RegSetValueExA(
        key,
        value_name.encode('utf-8'),
        0,
        value_type,
        value_data,
        len(value_data)
    )
    if result != 0:
        raise WindowsError("Error writing registry value: {}".format(result))


def delete_key(key_path, root_key=HKEY_LOCAL_MACHINE):
    result = ctypes.windll.advapi32.RegDeleteKeyA(
        root_key,
        key_path.encode('utf-8')
    )
    if result != 0:
        raise WindowsError("Error deleting registry key: {}".format(result))


def delete_value(key, value_name):
    result = ctypes.windll.advapi32.RegDeleteValueA(
        key,
        value_name.encode('utf-8')
    )
    if result != 0:
        raise WindowsError("Error deleting registry value: {}".format(result))


def close_key(key):
    ctypes.windll.advapi32.RegCloseKey(key)
