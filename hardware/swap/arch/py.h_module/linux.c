/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static PyObject * swap_memory(PyObject * self, PyObject * args) {
    FILE * meminfo = fopen("/proc/meminfo", "r");
    if (!meminfo) {
        return Py_BuildValue("(NNN)", Py_None, Py_None, Py_None);
    }

    long total_swap = 0;
    long free_swap = 0;
    char line[128];

    while (fgets(line, sizeof(line), meminfo)) {
        if (strncmp(line, "SwapTotal:", 10) == 0) {
            total_swap = atol(line + 10);
        } else if (strncmp(line, "SwapFree:", 9) == 0) {
            free_swap = atol(line + 9);
        }
    }

    fclose(meminfo);

    if (total_swap <= 0 || free_swap < 0) {
        return Py_BuildValue("(NNN)", Py_None, Py_None, Py_None);
    }

    long used_swap = total_swap - free_swap;

    long long total_swap_bytes = total_swap * 1024;
    long long used_swap_bytes = used_swap * 1024;
    long long free_swap_bytes = free_swap * 1024;

    return Py_BuildValue("(LLL)", total_swap_bytes, used_swap_bytes, free_swap_bytes);
}
