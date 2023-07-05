/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>

typedef DWORD (WINAPI * PFN_GetFirmwareEnvironmentVariableA) (
    LPCSTR lpName,
    LPCSTR lpGuid,
    PVOID pBuffer,
    DWORD nSize
);

const char * firmware() {
    HMODULE kernel32 = LoadLibraryA("kernel32.dll");
    if (kernel32 == NULL) {
        return "Unknown";
    }
    
    PFN_GetFirmwareEnvironmentVariableA pGetFirmwareEnvironmentVariableA = (PFN_GetFirmwareEnvironmentVariableA)GetProcAddress(kernel32, "GetFirmwareEnvironmentVariableA");
    
    char firmwareInfo[512];
    DWORD result = pGetFirmwareEnvironmentVariableA("SecureBoot", "{00000000-0000-0000-0000-000000000000}", firmwareInfo, sizeof(firmwareInfo));
    
    FreeLibrary(kernel32);
    
    return (result > 0) ? "UEFI" : "BIOS";
}
