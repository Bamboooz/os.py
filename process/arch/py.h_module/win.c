/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <Windows.h>
#include <TlHelp32.h>
#include <unistd.h>
#include <Python.h>

static PyObject * getpid(PyObject * self, PyObject * args) {
    int current_pid = GetCurrentProcessId();
    return PyLong_FromLong(current_pid);
}

static PyObject * pid_exists(PyObject * self, PyObject * args) {
    int pid;

    if (!PyArg_ParseTuple(args, "i", &pid)) {
        Py_RETURN_NONE;
    }

    
    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (snapshot == INVALID_HANDLE_VALUE) {
        Py_RETURN_NONE;
    }

    PROCESSENTRY32 processEntry;
    processEntry.dwSize = sizeof(PROCESSENTRY32);

    if (Process32First(snapshot, &processEntry)) {
        do {
            if (processEntry.th32ProcessID == (DWORD)pid) {
                CloseHandle(snapshot);
                Py_RETURN_TRUE;
            }
        } while (Process32Next(snapshot, &processEntry));
    }

    CloseHandle(snapshot);
    Py_RETURN_FALSE; // Process does not exist
}
