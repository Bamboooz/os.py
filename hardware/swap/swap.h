/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

#include "arch/windows/swap.c"

static PyMethodDef ospylib_hardware_swap_module_methods[] = {
    {"swap_memory", swap_memory, METH_NOARGS, "Get total swap memory."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef ospylib_hardware_swap_module = {
    PyModuleDef_HEAD_INIT,
    "ospylib_hardware_swap_module",
    NULL,
    -1,
    ospylib_hardware_swap_module_methods
};

PyMODINIT_FUNC PyInit_meminfo(void) {
    return PyModule_Create(&ospylib_hardware_swap_module);
}
