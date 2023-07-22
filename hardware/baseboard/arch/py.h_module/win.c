/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>

#include "../../../../common/regedit/registry.h"

static PyObject * product(PyObject * self, PyObject * args) {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardProduct", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return PyUnicode_FromString(buffer);
}

static PyObject * vendor(PyObject * self, PyObject * args) {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardManufacturer", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return PyUnicode_FromString(buffer);
}

static PyObject * version(PyObject * self, PyObject * args) {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardVersion", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return PyUnicode_FromString(buffer);
}
