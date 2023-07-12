/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Python.h>
#include <Windows.h>

#define BATTERY_STATUS_HIGH       0
#define BATTERY_STATUS_MEDIUM     1
#define BATTERY_STATUS_LOW        2
#define BATTERY_STATUS_CRITICAL   4
#define BATTERY_STATUS_CHARGING   8
#define BATTERY_STATUS_NO_BATTERY 128
#define BATTERY_STATUS_FAILED     255

static PyObject * percentage(PyObject * self, PyObject * args) {
    SYSTEM_POWER_STATUS powerStatus;

    if (GetSystemPowerStatus(&powerStatus))
    {
        if (powerStatus.BatteryLifePercent != BATTERY_PERCENTAGE_UNKNOWN)
        {
            return PyLong_FromLong(powerStatus.BatteryLifePercent);
        }
    }

    Py_RETURN_NONE;
}

static PyObject * charging(PyObject * self, PyObject * args) {
    SYSTEM_POWER_STATUS powerStatus;

    if (GetSystemPowerStatus(&powerStatus))
    {
        if (powerStatus.ACLineStatus == AC_LINE_ONLINE)
        {
            Py_RETURN_TRUE;
        }
        else if (powerStatus.ACLineStatus == AC_LINE_OFFLINE)
        {
            Py_RETURN_FALSE;
        }
    }

    Py_RETURN_NONE;
}

static PyObject * present(PyObject * self, PyObject * args) {
    SYSTEM_POWER_STATUS powerStatus;

    if (GetSystemPowerStatus(&powerStatus))
    {
        if (powerStatus.BatteryFlag & BATTERY_FLAG_NO_BATTERY)
        {
            Py_RETURN_FALSE;
        }
        else
        {
            Py_RETURN_TRUE;
        }
    }

    Py_RETURN_NONE;
}

static PyObject * flag(PyObject * self, PyObject * args) {
    /*
    Possible battery flags:
    Value	  Meaning
    0         High—the battery capacity is 66 percent or higher
    1         Medium—the battery percentage is higher or equal to 33 and lower than 66 percent
    2         Low—the battery percentage higher or equal to 5 and lower than 33 percent
    4         Critical—the battery percentage is at less than five percent
    8         Charging
    128       No system battery
    255       Unknown status—unable to read the battery flag information

    Using a custom flag system as the default one makes literally no sense.
    It makes values 33 to 66 percent not be detected as any flag returning None.

    Don't have to implement the not found as it is covered directly in sensors_battery()
    */
    SYSTEM_POWER_STATUS powerStatus;

    if (!GetSystemPowerStatus(&powerStatus)) {
        return PyLong_FromLong(BATTERY_STATUS_FAILED);
    }

    if (powerStatus.ACLineStatus == AC_LINE_ONLINE) {
        return PyLong_FromLong(BATTERY_STATUS_CHARGING);
    }

    int percentage = powerStatus.BatteryLifePercent;

    if (percentage == BATTERY_PERCENTAGE_UNKNOWN) {
        return PyLong_FromLong(BATTERY_STATUS_FAILED);
    }

    if (percentage < 5) {
        return PyLong_FromLong(BATTERY_STATUS_CRITICAL);
    }
    else if (percentage >= 5 && percentage < 33) {
        return PyLong_FromLong(BATTERY_STATUS_LOW);
    }
    else if (percentage >= 33 && percentage < 66) {
        return PyLong_FromLong(BATTERY_STATUS_MEDIUM);
    }
    else if (percentage >= 66) {
        return PyLong_FromLong(BATTERY_STATUS_HIGH);
    }

    return PyLong_FromLong(BATTERY_STATUS_FAILED);
}

static PyObject * battery_time(PyObject * self, PyObject * args) {
    SYSTEM_POWER_STATUS powerStatus;

    if (GetSystemPowerStatus(&powerStatus))
    {
        if (powerStatus.BatteryLifeTime != -1 && powerStatus.BatteryLifeTime != 0xFFFFFFFF)
        {
            return PyLong_FromLong(powerStatus.BatteryLifeTime);
        }
    }

    Py_RETURN_NONE;
}
