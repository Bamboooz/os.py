/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

#include "arch/windows/battery.c"

static PyMethodDef ospylib_battery_module_methods[] = {
    {"percentage", percentage, METH_NOARGS, "Get the battery percentage."},
    {"charging", charging, METH_NOARGS, "Check if the device is connected to a power source."},
    {"present", present, METH_NOARGS, "Check if a system battery is present."},
    {"flag", flag, METH_NOARGS, "Get the battery flag status."},
    {"time", battery_time, METH_NOARGS, "Get the battery time left."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef ospylib_battery_module = {
    PyModuleDef_HEAD_INIT,
    "ospylib_battery_module",
    NULL,
    -1,
    ospylib_battery_module_methods
};

PyMODINIT_FUNC PyInit_battery(void) {
    return PyModule_Create(&ospylib_battery_module);
}
