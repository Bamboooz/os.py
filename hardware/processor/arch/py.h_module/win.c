/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <stdio.h>
#include <Windows.h>

#include "../../../../common/cpuid/const.h"
#include "../../../../common/regedit/registry.h"
#include "../../../../common/types/dict.h"

static PyObject * model(PyObject * self, PyObject * args) {
    char buffer[256];
    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "ProcessorNameString", buffer, sizeof(buffer));

    if (result != 0) {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromString(buffer);
}

static PyObject * logical_cores(PyObject * self, PyObject * args) {
    SYSTEM_INFO sysInfo;
    GetSystemInfo(&sysInfo);
    return PyLong_FromLong(sysInfo.dwNumberOfProcessors);
}

static PyObject * physical_cores(PyObject * self, PyObject * args) {
    DWORD logicalProcessorCount = 0;
    DWORD physicalProcessorCount = 0;

    if (!GetLogicalProcessorInformation(NULL, &logicalProcessorCount)) {
        Py_RETURN_NONE; // Error
    }

    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION buffer = (PSYSTEM_LOGICAL_PROCESSOR_INFORMATION)malloc(logicalProcessorCount);

    if (!GetLogicalProcessorInformation(buffer, &logicalProcessorCount)) {
        free(buffer);
        Py_RETURN_NONE; // Error
    }

    DWORD byteOffset = 0;
    while (byteOffset + sizeof(SYSTEM_LOGICAL_PROCESSOR_INFORMATION) <= logicalProcessorCount) {
        PSYSTEM_LOGICAL_PROCESSOR_INFORMATION item = (PSYSTEM_LOGICAL_PROCESSOR_INFORMATION)((BYTE*)buffer + byteOffset);
        if (item->Relationship == RelationProcessorCore) {
            physicalProcessorCount++;
        }
        byteOffset += sizeof(SYSTEM_LOGICAL_PROCESSOR_INFORMATION);
    }

    free(buffer);
    return PyLong_FromLong(physicalProcessorCount);
}

static PyObject * architecture(PyObject * self, PyObject * args) {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment", "PROCESSOR_ARCHITECTURE", buffer, sizeof(buffer));

    if (result != 0) {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromString(buffer);
}

static PyObject * clockspeed(PyObject * self, PyObject * args) {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "~MHz", buffer, sizeof(buffer));

    if (result != 0) {
        Py_RETURN_NONE;
    }

    return PyLong_FromLong(atoi(buffer));
}

static PyObject * vendor(PyObject * self, PyObject * args) {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "VendorIdentifier", buffer, sizeof(buffer));

    if (result != 0) {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromString(buffer);
}

static PyObject * manufacturer(PyObject * self, PyObject * args) {
    PyObject * vendor_result = vendor(self, args); // Call the vendor function directly
    if (vendor_result == NULL || vendor_result == Py_None) {
        Py_XDECREF(vendor_result);
        Py_RETURN_NONE; // Or return any other default value if vendor returns None or has an error
    }

    char * vendor_str = PyUnicode_AsUTF8(vendor_result);
    Py_XDECREF(vendor_result);

    size_t dict_size = sizeof(vmap_manufacturer) / sizeof(vmap_manufacturer[0]);
    char * manufacturer = value_from_dict(vmap_manufacturer, dict_size, vendor_str, "");

    return PyUnicode_FromString(manufacturer);
}

static PyObject * cpu_type(PyObject * self, PyObject * args) {
    PyObject * vendor_result = vendor(self, args); // Call the vendor function directly
    if (vendor_result == NULL || vendor_result == Py_None) {
        Py_XDECREF(vendor_result);
        Py_RETURN_NONE; // Or return any other default value if vendor returns None or has an error
    }

    char * vendor_str = PyUnicode_AsUTF8(vendor_result);
    Py_XDECREF(vendor_result);

    size_t dict_size = sizeof(vmap_type) / sizeof(vmap_type[0]);
    char * cpu_type = value_from_dict(vmap_type, dict_size, vendor_str, "");

    return PyUnicode_FromString(cpu_type);
}
