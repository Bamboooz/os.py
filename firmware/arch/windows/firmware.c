/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>

#include "../../../common/regedit/registry.h"

char * firmware() {
    HMODULE kernel32 = LoadLibraryA("kernel32.dll");
    if (kernel32 == NULL) {
        return NULL;
    }

    typedef DWORD (WINAPI * PFN_GetFirmwareEnvironmentVariableA)(LPCSTR, LPCSTR, PVOID, DWORD);

    PFN_GetFirmwareEnvironmentVariableA pGetFirmwareEnvironmentVariableA = (PFN_GetFirmwareEnvironmentVariableA)GetProcAddress(kernel32, "GetFirmwareEnvironmentVariableA");
    if (pGetFirmwareEnvironmentVariableA == NULL) {
        FreeLibrary(kernel32);
        return NULL;
    }

    char firmwareInfo[512];
    DWORD result = pGetFirmwareEnvironmentVariableA("SecureBoot", "{00000000-0000-0000-0000-000000000000}", firmwareInfo, sizeof(firmwareInfo));

    FreeLibrary(kernel32);

    const char * firmwareType = (result > 0) ? "UEFI" : "BIOS";
    return firmwareType;
}

char * version() {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "BIOSVersion", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return buffer;
}

char * release_date() {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "BIOSReleaseDate", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return buffer;
}

char * vendor() {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BIOSVendor", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return buffer;
}
