/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <Windows.h>

static PyObject * resolution(PyObject * self, PyObject * args) {
    int x = GetSystemMetrics(SM_CXSCREEN);
    int y = GetSystemMetrics(SM_CYSCREEN);
    return Py_BuildValue("ii", x, y);
}

static PyObject * refreq(PyObject * self, PyObject * args) {
    DEVMODE devMode;
    memset(&devMode, 0, sizeof(devMode));
    devMode.dmSize = sizeof(devMode);

    if (EnumDisplaySettings(NULL, ENUM_CURRENT_SETTINGS, &devMode)) {
        return PyLong_FromLong(devMode.dmDisplayFrequency);
    }

    return PyLong_FromLong(-1);
}
