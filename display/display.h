/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include "arch/windows/display.c"

static PyMethodDef ospylib_display_module_methods[] = {
    {"resolution", resolution, METH_NOARGS, "Get the screen resolution as a tuple (x, y)."},
    {"refreq", refreq, METH_NOARGS, "Get the screen refresh rate."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef ospylib_display_module = {
    PyModuleDef_HEAD_INIT,
    "ospylib_display_module",
    NULL,
    -1,
    ospylib_display_module_methods
};

PyMODINIT_FUNC PyInit_display(void) {
    return PyModule_Create(&ospylib_display_module);
}
