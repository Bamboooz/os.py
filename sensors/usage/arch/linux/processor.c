/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

static PyObject * cpu_percent(PyObject * self, PyObject * args) {
    PyObject * percpu_obj;

    if (!PyArg_ParseTuple(args, "O", &percpu_obj)) {
        return NULL;
    }

    int percpu = PyObject_IsTrue(percpu_obj);
}
