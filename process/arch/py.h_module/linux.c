/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <unistd.h>
#include <stdio.h>
#include <Python.h>

static PyObject * getpid(PyObject * self, PyObject * args) {
    int current_pid = getpid();
    return PyLong_FromLong(current_pid);
}

static PyObject * pid_exists(PyObject * self, PyObject * args) {
    int pid;

    if (!PyArg_ParseTuple(args, "i", &pid)) {
        Py_RETURN_NONE;
    }

    char path[64];
    snprintf(path, sizeof(path), "/proc/%d", pid);
    
    if (access(path, F_OK) == 0) {
        Py_RETURN_TRUE;
    }
    
    Py_RETURN_FALSE;
}
