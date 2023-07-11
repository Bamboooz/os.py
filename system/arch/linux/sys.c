/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <unistd.h>

static PyObject * is_admin(PyObject * self, PyObject * args) {
    int isAdmin = geteuid() == 0;
    return PyBool_FromLong(isAdmin);
}

static PyObject * uptime(PyObject * self, PyObject * args) {
    FILE * file = fopen("/proc/uptime", "r");
    if (!file) {
        PyErr_SetString(PyExc_IOError, "Failed to open /proc/uptime");
        return NULL;
    }

    double uptimeValue;
    if (fscanf(file, "%lf", &uptimeValue) != 1) {
        fclose(file);
        PyErr_SetString(PyExc_IOError, "Failed to read /proc/uptime");
        return NULL;
    }

    fclose(file);
    return PyLong_FromLong((long)uptimeValue);
}
