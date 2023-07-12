/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <Windows.h>

static PyObject * swap_percent(PyObject * self, PyObject * args) {
    MEMORYSTATUSEX status;
    status.dwLength = sizeof(status);
    
    if (!GlobalMemoryStatusEx(&status)) {
        Py_RETURN_NONE;
    }

    double totalSwap = (double)status.ullTotalPageFile;
    double usedSwap = totalSwap - (double)status.ullAvailPageFile; // used = total - free swap

    double swapUsage = (usedSwap / totalSwap) * 100.0;
    return PyFloat_FromDouble(swapUsage);
}
