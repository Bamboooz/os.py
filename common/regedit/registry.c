/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <windows.h>

char * read_registry_value(HKEY hKey, const char * subKey, const char * valueName) {
    HKEY hKeyResult;
    if (RegOpenKeyExA(hKey, subKey, 0, KEY_READ, &hKeyResult) != ERROR_SUCCESS)
        return NULL; // Failed to open the registry key

    DWORD valueType;
    DWORD bufferSize = 0;
    if (RegQueryValueExA(hKeyResult, valueName, NULL, &valueType, NULL, &bufferSize) != ERROR_SUCCESS || valueType != REG_SZ) {
        RegCloseKey(hKeyResult);
        return NULL; // Failed to retrieve the value size or value is not of type REG_SZ
    }

    // Allocate memory for the value
    char * buffer = _strdup(""); // Initialize with an empty string to ensure valid pointer even if the value is empty
    if (buffer == NULL) {
        RegCloseKey(hKeyResult);
        return NULL; // Memory allocation failed
    }

    // Resize the buffer to the actual value size
    buffer = realloc(buffer, bufferSize);
    if (buffer == NULL) {
        RegCloseKey(hKeyResult);
        return NULL; // Memory allocation failed
    }

    // Retrieve the value
    if (RegQueryValueExA(hKeyResult, valueName, NULL, &valueType, (LPBYTE)buffer, &bufferSize) != ERROR_SUCCESS || valueType != REG_SZ) {
        RegCloseKey(hKeyResult);
        free(buffer);
        return NULL; // Failed to retrieve the value or value is not of type REG_SZ
    }

    RegCloseKey(hKeyResult);
    return buffer;
}

int count_subkeys(HKEY hKey, const char * subKey) {
    HKEY hKeyResult;
    if (RegOpenKeyExA(hKey, subKey, 0, KEY_READ, &hKeyResult) != ERROR_SUCCESS)
        return -1; // Failed to open the registry key

    DWORD numSubkeys;
    if (RegQueryInfoKeyA(hKeyResult, NULL, NULL, NULL, &numSubkeys, NULL, NULL, NULL, NULL, NULL, NULL, NULL) != ERROR_SUCCESS) {
        RegCloseKey(hKeyResult);
        return -1; // Failed to retrieve the number of subkeys
    }

    RegCloseKey(hKeyResult);
    return numSubkeys;
}
