/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <locale.h>
#include <sys/utsname.h>
#include <Python.h>

#define SYSTEM_INFORMATION_BUFFER 256

static PyObject * hostname(PyObject * self, PyObject * args) {
    static char hostname[SYSTEM_INFORMATION_BUFFER];

    if (gethostname(hostname, sizeof(hostname)) != 0) {
        Py_RETURN_NONE;
    }

    return PyUnicode_FromString(hostname);
}

static PyObject * version(PyObject * self, PyObject * args) {
    struct utsname info;

    if (uname(&info) != 0) {
        Py_RETURN_NONE;
    }

    static char version[SYSTEM_INFORMATION_BUFFER];
    snprintf(version, sizeof(version), "%s", info.version);
    return PyUnicode_FromString(version);
}

static PyObject * platform(PyObject * self, PyObject * args) {
    struct utsname info;

    if (uname(&info) != 0) {
        Py_RETURN_NONE;
    }

    static char platform[SYSTEM_INFORMATION_BUFFER];
    snprintf(platform, sizeof(platform), "%s-%s-%s", info.sysname, info.release, info.machine);
    return PyUnicode_FromString(platform);
}

static PyObject * release(PyObject * self, PyObject * args) {
    struct utsname info;

    if (uname(&info) != 0) {
        Py_RETURN_NONE;
    }

    static char release[SYSTEM_INFORMATION_BUFFER];
    snprintf(release, sizeof(release), "%s", info.release);
    return PyUnicode_FromString(release);
}

static PyObject * arch(PyObject * self, PyObject * args) {
    struct utsname info;

    if (uname(&info) != 0) {
        Py_RETURN_NONE;
    }

    static char machine[SYSTEM_INFORMATION_BUFFER];
    snprintf(machine, sizeof(machine), "%s", info.machine);
    return PyUnicode_FromString(machine);
}

static PyObject * user(PyObject * self, PyObject * args) {
    char * username = getenv("USERNAME");
    int isAdmin = geteuid() == 0;

    return Py_BuildValue("(OO)", username, isAdmin);
}

static PyObject * lang(PyObject * self, PyObject * args) {
    setlocale(LC_ALL, "");
    char * lang_env = getenv("LANG");
    char * encoding = NULL;

    if (lang_env != NULL) {
        char * dot = strchr(lang_env, '.');
        if (dot != NULL) {
            *dot = '\0';
            encoding = dot + 1;
        }
    }

    return Py_BuildValue("(OO)", lang_env, encoding);
}

static PyObject * uptime(PyObject * self, PyObject * args) {
    FILE * file = fopen("/proc/uptime", "r");

    if (!file) {
        Py_RETURN_NONE;
    }

    double uptimeValue;
    
    if (fscanf(file, "%lf", &uptimeValue) != 1) {
        fclose(file);
        Py_RETURN_NONE;
    }

    fclose(file);
    return PyLong_FromLong((long)uptimeValue);
}
