/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <unistd.h>

static PyObject * firmware(PyObject * self, PyObject * args) {
    int is_uefi = (access("/sys/firmware/efi", F_OK) == 0) ? 1 : 0;
    const char * firmwareType = is_uefi ? "UEFI" : "BIOS";
    return PyUnicode_FromString(firmwareType);
}
