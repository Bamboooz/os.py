/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

#ifdef _WIN32
    #include "arch/windows/swap.c"
#elif __linux__
    #include "arch/linux/swap.c"
#endif

static PyMethodDef ospylib_swap_module_methods[] = {
    {"total", total, METH_NOARGS, "Get total swap memory."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef ospylib_swap_module = {
    PyModuleDef_HEAD_INIT,
    "ospylib_swap_module",
    NULL,
    -1,
    ospylib_swap_module_methods
};

PyMODINIT_FUNC PyInit_meminfo(void) {
    return PyModule_Create(&ospylib_swap_module);
}
