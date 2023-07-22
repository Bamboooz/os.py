/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <stdio.h>
#include <Windows.h>

static PyObject * swap_memory(PyObject * self, PyObject * args) {
    MEMORYSTATUSEX status;
    status.dwLength = sizeof(status);

    if (!GlobalMemoryStatusEx(&status)) {
        Py_RETURN_NONE;
    }

    long long totalSwap = (long long)status.ullTotalPageFile;
    long long freeSwap = (long long)status.ullAvailPageFile;
    long long usedSwap = totalSwap - freeSwap;

    return Py_BuildValue("(LLL)", totalSwap, usedSwap, freeSwap);
}
