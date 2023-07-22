/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <Windows.h>
#include <stdbool.h>
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SYSTEM_INFORMATION_BUFFER 256
#define LANG_BUFFER_SIZE 256

static PyObject * hostname(PyObject * self, PyObject * args) {
    static char hostname[SYSTEM_INFORMATION_BUFFER];
    DWORD length = sizeof(hostname);

    if (!GetComputerNameA(hostname, &length)) {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromString(hostname);
}

static PyObject * version(PyObject * self, PyObject * args) {
    OSVERSIONINFOEX osvi;
    ZeroMemory(&osvi, sizeof(OSVERSIONINFOEX));
    osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);

    if (GetVersionEx((OSVERSIONINFO*)&osvi) == 0) {
        Py_RETURN_NONE;
    }

    static char version[SYSTEM_INFORMATION_BUFFER];
    snprintf(version, sizeof(version), "%d.%d.%d", osvi.dwMajorVersion, osvi.dwMinorVersion, osvi.dwBuildNumber);

    return PyUnicode_FromString(version);
}

static PyObject * platform(PyObject * self, PyObject * args) {
    OSVERSIONINFOEX osvi;
    ZeroMemory(&osvi, sizeof(OSVERSIONINFOEX));
    osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);

    if (GetVersionEx((OSVERSIONINFO*)&osvi) == 0) {
        Py_RETURN_NONE;
    }

    char release[128];
    snprintf(release, sizeof(release), "%d.%d.%d", osvi.dwMajorVersion, osvi.dwMinorVersion, osvi.dwBuildNumber);

    char machine[SYSTEM_INFORMATION_BUFFER];
    DWORD machineSize = sizeof(machine);
    if (GetEnvironmentVariable("PROCESSOR_ARCHITECTURE", machine, machineSize) == 0) {
        Py_RETURN_NONE;
    }

    static char platform[SYSTEM_INFORMATION_BUFFER];
    snprintf(platform, sizeof(platform), "Windows-%s-%s", release, machine);

    return PyUnicode_FromString(platform);
}

static PyObject * release(PyObject * self, PyObject * args) {
    OSVERSIONINFOEX osvi;
    ZeroMemory(&osvi, sizeof(OSVERSIONINFOEX));
    osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);

    if (GetVersionEx((OSVERSIONINFO*)&osvi) == 0) {
        Py_RETURN_NONE;
    }

    static char result[SYSTEM_INFORMATION_BUFFER];
    snprintf(result, sizeof(result), "%d.%d.%d", osvi.dwMajorVersion, osvi.dwMinorVersion, osvi.dwBuildNumber);

    return PyUnicode_FromString(result);
}

static PyObject * arch(PyObject * self, PyObject * args) {
    static char machine[SYSTEM_INFORMATION_BUFFER];
    DWORD machineSize = sizeof(machine);

    if (GetEnvironmentVariable("PROCESSOR_ARCHITECTURE", machine, machineSize) == 0) {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromString(machine);
}

static PyObject * user(PyObject * self, PyObject * args) {
    const char * username = getenv("USERNAME");
    int isAdmin = geteuid() == 0;

    return Py_BuildValue("(sO)", username, isAdmin ? Py_True : Py_False);
}

static PyObject * lang(PyObject * self, PyObject * args) {
    setlocale(LC_ALL, "");
    static char lang_env[LANG_BUFFER_SIZE];
    char * env = getenv("LANG");
    if (env == NULL) {
        Py_RETURN_NONE;
    }
    snprintf(lang_env, LANG_BUFFER_SIZE, "%s", env);
    char* dot = strchr(lang_env, '.');
    if (dot != NULL) {
        *dot = '\0';
    }

    UINT codePage = GetACP();
    static char encoding[32];
    snprintf(encoding, sizeof(encoding), "cp%d", codePage);

    return Py_BuildValue("(sO)", lang_env, PyUnicode_FromString(encoding));
}

static PyObject * uptime(PyObject * self, PyObject * args) {
    DWORD ticks = GetTickCount();
    int seconds = ticks / 1000;
    return PyLong_FromLong(seconds);
}

static PyObject * safe_mode(PyObject * self, PyObject * args) {
    int inSafeMode = GetSystemMetrics(SM_CLEANBOOT) != 0;
    return PyBool_FromLong((long)inSafeMode);
}

static PyObject * hvci(PyObject * self, PyObject * args) {
    int hvciEnabled = 0;
    HMODULE kernel32 = GetModuleHandleA("kernel32.dll");
    typedef BOOL(WINAPI* PIsHvciEnabled)();

    if (kernel32) {
        FARPROC proc = GetProcAddress(kernel32, "IsHvciEnabled");
        PIsHvciEnabled pIsHvciEnabled = (PIsHvciEnabled)proc;
        hvciEnabled = (pIsHvciEnabled != NULL) ? pIsHvciEnabled() : 0;
    }

    return PyBool_FromLong((long)hvciEnabled);
}
