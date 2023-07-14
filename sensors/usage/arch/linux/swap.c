/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

#define SWAP_INFORMATION_BUFFER 256

static PyObject * swap_percent(PyObject * self, PyObject * args) {
    FILE * meminfo = fopen("/proc/meminfo", "r");

    if (meminfo == NULL) {
        Py_RETURN_NONE;
    }

    char buffer[SWAP_INFORMATION_BUFFER];
    long totalSwap = 0;
    long freeSwap = 0;

    while (fgets(buffer, sizeof(buffer), meminfo)) {
        sscanf(buffer, "SwapTotal: %ld kB", &totalSwap);
        sscanf(buffer, "SwapFree: %ld kB", &freeSwap);
    }

    fclose(meminfo);

    if (totalSwap < 0 || freeSwap < 0) {
        Py_RETURN_NONE;
    }

    long usedSwap = totalSwap - freeSwap;
    double swapUsage = ((double)usedSwap / (double)totalSwap) * 100.0;
    
    return PyFloat_FromDouble(swapUsage);
}