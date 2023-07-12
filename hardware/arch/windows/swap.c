/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <stdio.h>
#include <windows.h>

static PyObject * total(PyObject * self, PyObject * args) {
    MEMORYSTATUSEX status;
    status.dwLength = sizeof(status);

    if (GlobalMemoryStatusEx(&status)) {
        long totalSwap = (long)status.ullTotalPageFile;
        return PyLong_FromLong(totalSwap);
    }

    Py_RETURN_NONE;
}
