/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

#if _WIN32
    #include "arch/windows/firmware.c"
#elif __linux__
    #include "arch/linux/firmware.c"
#endif

static PyMethodDef ospylib_firmware_module_methods[] = {
    {"firmware", firmware, METH_NOARGS, "Check if the system is using UEFI or BIOS firmware."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef ospylib_firmware_module = {
    PyModuleDef_HEAD_INIT,
    "ospylib_firmware_module",
    NULL,
    -1,
    ospylib_firmware_module_methods
};

PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&ospylib_firmware_module);
}
