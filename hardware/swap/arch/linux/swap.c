/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

#define SWAP_INFORMATION_BUFFER 256

static PyObject * swap_memory(PyObject * self, PyObject * args) {
    FILE * meminfo = fopen("/proc/meminfo", "r");

    if (meminfo == NULL) {
        Py_RETURN_NONE;
    }

    char buffer[SWAP_INFORMATION_BUFFER];
    long long totalSwap = 0;
    long long freeSwap = 0;

    while (fgets(buffer, sizeof(buffer), meminfo)) {
        sscanf(buffer, "SwapTotal: %lld", &totalSwap);
        sscanf(buffer, "SwapFree: %lld", &freeSwap);
    }

    fclose(meminfo);

    if (totalSwap < 0 || freeSwap < 0) {
        Py_RETURN_NONE;
    }

    long long usedSwap = totalSwap - freeSwap;

    return Py_BuildValue("(LLL)", totalSwap * 1024, usedSwap * 1024, freeSwap * 1024);  // Convert to bytes
}
