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

static PyObject * swap_percent(PyObject * self, PyObject * args) {
    FILE * meminfo = fopen("/proc/meminfo", "r");
    if (!meminfo) {
        Py_RETURN_NONE; // Error opening file
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

    if (total_swap <= 0 || free_swap <= 0) {
        Py_RETURN_NONE; // Invalid swap values
    }

    long used_swap = total_swap - free_swap;
    double swap_usage = ((double)used_swap / total_swap) * 100.0;

    return PyFloat_FromDouble(swap_usage);
}

static PyObject * cpu_percent(PyObject * self, PyObject * args) {
    PyObject * percpu_obj;

    if (!PyArg_ParseTuple(args, "O", &percpu_obj)) {
        return NULL;
    }

    int percpu = PyObject_IsTrue(percpu_obj);
}

static PyObject * memory_percent(PyObject * self, PyObject * args) {
    FILE * meminfo = fopen("/proc/meminfo", "r");
    if (!meminfo) {
        Py_RETURN_NONE; // Error opening file
    }

    long total_memory = 0;
    long free_memory = 0;
    char line[128];

    while (fgets(line, sizeof(line), meminfo)) {
        if (strncmp(line, "MemTotal:", 9) == 0) {
            total_memory = atol(line + 9);
        } else if (strncmp(line, "MemFree:", 8) == 0) {
            free_memory = atol(line + 8);
        }
    }

    fclose(meminfo);

    if (total_memory <= 0 || free_memory <= 0) {
        Py_RETURN_NONE; // Invalid memory values
    }

    long used_memory = total_memory - free_memory;
    double memory_usage = ((double)used_memory / total_memory) * 100.0;

    return PyFloat_FromDouble(memory_usage);
}

static PyObject * gpu_percent(PyObject * self, PyObject * args) {

}
