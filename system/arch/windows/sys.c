/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <Windows.h>

typedef BOOL (WINAPI * PIsHvciEnabled)();

static PyObject * is_admin(PyObject * self, PyObject * args) {
    BOOL isAdmin = FALSE;
    SID_IDENTIFIER_AUTHORITY ntAuthority = SECURITY_NT_AUTHORITY;
    PSID administratorsGroup;

    if (AllocateAndInitializeSid(&ntAuthority, 2, SECURITY_BUILTIN_DOMAIN_RID, DOMAIN_ALIAS_RID_ADMINS, 0, 0, 0, 0, 0, 0, &administratorsGroup)) {
        if (!CheckTokenMembership(NULL, administratorsGroup, &isAdmin)) {
            isAdmin = FALSE;
        }
        FreeSid(administratorsGroup);
    }

    return PyBool_FromLong((long)isAdmin);
}

static PyObject * uptime(PyObject * self, PyObject * args) {
    DWORD ticks = GetTickCount();
    double seconds = (double)ticks / 1000.0;
    return PyFloat_FromDouble(seconds);
}

static PyObject * safe_mode(PyObject * self, PyObject * args) {
    BOOL inSafeMode = GetSystemMetrics(SM_CLEANBOOT) != 0;
    return PyBool_FromLong((long)inSafeMode);
}

static PyObject * hvci(PyObject * self, PyObject * args) {
    int hvciEnabled = 0;
    HMODULE kernel32 = GetModuleHandleA("kernel32.dll");
    if (kernel32) {
        FARPROC proc = GetProcAddress(kernel32, "IsHvciEnabled");
        PIsHvciEnabled pIsHvciEnabled = (PIsHvciEnabled)proc;
        hvciEnabled = (pIsHvciEnabled != NULL) ? pIsHvciEnabled() : 0;
    }
    return PyBool_FromLong((long)hvciEnabled);
}
