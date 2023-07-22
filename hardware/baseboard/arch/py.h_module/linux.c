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

char * read_smbios_file(const char * filepath) {
    FILE * file = fopen(filepath, "r");
    if (file == NULL) {
        return NULL;
    }

    char * buffer = NULL;
    size_t read_size = getline(&buffer, &(size_t){0}, file);
    if (read_size == -1) {
        free(buffer);
        fclose(file);
        return NULL;
    }

    buffer[strcspn(buffer, "\n")] = '\0';

    fclose(file);
    return buffer;
}

static PyObject * product(PyObject * self, PyObject * args) {
    char * product_name = read_smbios_file("/sys/class/dmi/id/board_name");
    return PyUnicode_FromString(product_name);
}

static PyObject * vendor(PyObject * self, PyObject * args) {
    char * vendor_name = read_smbios_file("/sys/class/dmi/id/board_vendor");
    return PyUnicode_FromString(vendor_name);
}

static PyObject * version(PyObject * self, PyObject * args) {
    char * version_name = read_smbios_file("/sys/class/dmi/id/board_version");
    return PyUnicode_FromString(version_name);
}
