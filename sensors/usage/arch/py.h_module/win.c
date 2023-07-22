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

static PyObject * cpu_percent(PyObject * self, PyObject * args) {
    PyObject * percpu_obj;

    if (!PyArg_ParseTuple(args, "O", &percpu_obj)) {
        return NULL;
    }

    int percpu = PyObject_IsTrue(percpu_obj);
}

static PyObject * memory_percent(PyObject * self, PyObject * args) {
    MEMORYSTATUSEX status;
    status.dwLength = sizeof(status);

    if (!GlobalMemoryStatusEx(&status)) {
        Py_RETURN_NONE;
    }

    double totalMemory = (double)status.ullTotalPhys;
    double usedMemory = totalMemory - (double)status.ullAvailPhys; // used = total - free memory

    double memoryUsage = (usedMemory / totalMemory) * 100.0;

    return PyFloat_FromDouble(memoryUsage);
}

static PyObject * gpu_percent(PyObject * self, PyObject * args) {

}
