/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <Python.h>

#ifdef _WIN32
    #define OPERATING_SYSTEM "Windows"
#elif __linux__
    #define OPERATING_SYSTEM "Linux"
#endif

static PyObject * name(PyObject * self, PyObject * args) {
    return PyUnicode_FromString(OPERATING_SYSTEM);
}
