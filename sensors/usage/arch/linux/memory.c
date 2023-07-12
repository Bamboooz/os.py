/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

#define MEMORY_INFORMATION_BUFFER 256

static PyObject * memory_percent(PyObject * self, PyObject * args) {
    FILE * meminfo = fopen("/proc/meminfo", "r");

    if (meminfo == NULL) {
        Py_RETURN_NONE;
    }

    char buffer[MEMORY_INFORMATION_BUFFER];
    long totalMemory = 0;
    long freeMemory = 0;

    while (fgets(buffer, sizeof(buffer), meminfo)) {
        sscanf(buffer, "MemTotal: %ld kB", &totalMemory);
        sscanf(buffer, "MemFree: %ld kB", &freeMemory);
    }

    fclose(meminfo);

    if (totalMemory < 0 || freeMemory < 0) {
        Py_RETURN_NONE;
    }

    long usedMemory = totalMemory - freeMemory;
    double memoryUsage = ((double)usedMemory / (double)totalMemory) * 100.0;
    
    return PyFloat_FromDouble(memoryUsage);
}
