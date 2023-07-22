/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <Python.h>

#ifdef _WIN32
    #define OPERATING_SYSTEM "Windows"
    #include "arch/windows/sys.c"
#elif __linux__
    #define OPERATING_SYSTEM "Linux"
    #include "arch/linux/sys.c"
#endif

const char * name() {
    return OPERATING_SYSTEM;
}

static PyMethodDef ospylib_system_module_methods[] = {
    {"name", name, METH_NOARGS, "Returns the system/OS name, e.g. 'Linux' or 'Windows'"},
    {"hostname", hostname, METH_NOARGS, "Returns the computer's network name (which may not be fully qualified)"},
    {"version", version, METH_NOARGS, "Returns the system's release version, e.g. '#3 on degas'"},
    {"platform", platform, METH_NOARGS, "Returns a single string identifying the underlying platform with as much useful information as possible (but no more :)."},
    {"release", release, METH_NOARGS, "Returns the system's release, e.g. '2.2.0' or 'NT'"},
    {"arch", arch, METH_NOARGS, "Returns the architecture of the running operating system."},
    {"user", user, METH_NOARGS, "Returns a tuple with current system user and is that user an administrator e.g. ('bamboooz', True)."},
    {"lang", lang, METH_NOARGS, "Returns a tuple with system langauge and preferred encoding system e.g. ('en_EN', 'UTF-8')."},
    {"uptime", uptime, METH_NOARGS, "Get the system uptime in seconds."},
#ifdef _WIN32
    {"safe_mode", safe_mode, METH_NOARGS, "Check if the system is in safe mode."},
    {"hvci", hvci, METH_NOARGS, "Check if HVCI (Hypervisor-Protected Code Integrity) is enabled."},
#endif
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef ospylib_system_module = {
    PyModuleDef_HEAD_INIT,
    "ospylib_system_module",
    NULL,
    -1,
    ospylib_system_module_methods
};

PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&ospylib_system_module);
}
