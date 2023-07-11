/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#if _WIN32
    #include "arch/windows/sys.c"
#elif __linux__
    #include "arch/linux/sys.c"
#endif

static PyMethodDef ospylib_system_module_methods[] = {
    {"is_admin", is_admin, METH_NOARGS, "Check if the current user is an administrator."},
    {"uptime", uptime, METH_NOARGS, "Get the system uptime in seconds."},
#if _WIN32
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
