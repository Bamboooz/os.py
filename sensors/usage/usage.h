/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

#if _WIN32
    #include "arch/windows/swap.c"
    #include "arch/windows/memory.c"
    #include "arch/windows/graphics.c"
    #include "arch/windows/processor.c"
#elif __linux__
    #include "arch/linux/swap.c"
    #include "arch/linux/memory.c"
    #include "arch/linux/graphics.c"
    #include "arch/linux/processor.c"
#endif

static PyMethodDef ospylib_sensors_usage_module_methods[] = {
    {"cpu_percent", cpu_percent, METH_VARARGS, "Get CPU usage in percent."},
    {"swap_percent", swap_percent, METH_NOARGS, "Calculate swap usage in percent."},
    {"memory_percent", memory_percent, METH_NOARGS, "Calculate ram usage in percent."},
    {"gpu_percent", gpu_percent, METH_NOARGS, "Get GPU usage in percent."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef ospylib_sensors_usage_module = {
    PyModuleDef_HEAD_INIT,
    "ospylib_sensors_usage_module",
    NULL,
    -1,
    ospylib_sensors_usage_module_methods
};

PyMODINIT_FUNC PyInit_my_module(void) {
    return PyModule_Create(&ospylib_sensors_usage_module);
}
