/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <Windows.h>

#include "../../../common/regedit/registry.h"

static PyObject * firmware(PyObject * self, PyObject * args) {
    HMODULE kernel32 = LoadLibraryA("kernel32.dll");
    if (kernel32 == NULL) {
        Py_RETURN_NONE;
    }

    typedef DWORD (WINAPI * PFN_GetFirmwareEnvironmentVariableA)(LPCSTR, LPCSTR, PVOID, DWORD);

    PFN_GetFirmwareEnvironmentVariableA pGetFirmwareEnvironmentVariableA = (PFN_GetFirmwareEnvironmentVariableA)GetProcAddress(kernel32, "GetFirmwareEnvironmentVariableA");
    if (pGetFirmwareEnvironmentVariableA == NULL) {
        FreeLibrary(kernel32);
        Py_RETURN_NONE;
    }

    char firmwareInfo[512];
    DWORD result = pGetFirmwareEnvironmentVariableA("SecureBoot", "{00000000-0000-0000-0000-000000000000}", firmwareInfo, sizeof(firmwareInfo));

    FreeLibrary(kernel32);

    const char * firmwareType = (result > 0) ? "UEFI" : "BIOS";
    return PyUnicode_FromString(firmwareType);
}

static PyObject * version(PyObject * self, PyObject * args) {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "BIOSVersion", buffer, sizeof(buffer));

    if (result != 0) {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromString(buffer);
}

static PyObject * release_date(PyObject * self, PyObject * args) {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "BIOSReleaseDate", buffer, sizeof(buffer));

    if (result != 0) {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromString(buffer);
}

static PyObject * vendor(PyObject * self, PyObject * args) {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BIOSVendor", buffer, sizeof(buffer));

    if (result != 0) {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromString(buffer);
}
