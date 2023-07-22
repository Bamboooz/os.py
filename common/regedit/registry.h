/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>
#include <stdio.h>

int read_registry_value(HKEY hBaseKey, const char * subKey, const char * valueName, char * buffer, DWORD bufferSize) {
    HKEY hKey;
    LONG result = RegOpenKeyEx(hBaseKey, subKey, 0, KEY_READ, &hKey);
    if (result != ERROR_SUCCESS) {
        return 1;
    }

    DWORD dataSize = bufferSize;
    result = RegQueryValueEx(hKey, valueName, NULL, NULL, (BYTE*)buffer, &dataSize);
    if (result != ERROR_SUCCESS) {
        RegCloseKey(hKey);
        return 1;
    }

    RegCloseKey(hKey);

    return 0;
}
