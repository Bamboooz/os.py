/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

static PyObject * firmware(PyObject * self, PyObject * args) {
    int is_uefi = access("/sys/firmware/efi", F_OK);
    const char * firmware_type = is_uefi ? "UEFI" : "BIOS";
    return PyUnicode_FromString(firmware_type);
}

static PyObject * version(PyObject * self, PyObject * args) {
    FILE * dmi_file = fopen("/sys/class/dmi/id/bios_version", "r");
    if (!dmi_file) {
        Py_RETURN_NONE;
    }

    char version[128];
    fgets(version, sizeof(version), dmi_file);
    fclose(dmi_file);

    return PyUnicode_FromString(version);
}

static PyObject * release_date(PyObject * self, PyObject * args) {
    FILE * dmi_file = fopen("/sys/class/dmi/id/bios_release", "r");
    if (!dmi_file) {
        Py_RETURN_NONE;
    }

    char release_date[128];
    fgets(release_date, sizeof(release_date), dmi_file);
    fclose(dmi_file);

    return PyUnicode_FromString(release_date);
}

static PyObject * vendor(PyObject * self, PyObject * args) {
    FILE * dmi_file = fopen("/sys/class/dmi/id/bios_vendor", "r");
    if (!dmi_file) {
        Py_RETURN_NONE;
    }

    char vendor[128];
    fgets(vendor, sizeof(vendor), dmi_file);
    fclose(dmi_file);

    return PyUnicode_FromString(vendor);
}
