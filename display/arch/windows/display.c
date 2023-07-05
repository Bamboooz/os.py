/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <windows.h>

const int x_res() {
    return GetSystemMetrics(SM_CXSCREEN);
}

const int y_res() {
    return GetSystemMetrics(SM_CYSCREEN);
}

const int refreq() {
    DEVMODE devMode;
    memset(&devMode, 0, sizeof(devMode));
    devMode.dmSize = sizeof(devMode);

    if (EnumDisplaySettings(NULL, ENUM_CURRENT_SETTINGS, &devMode)) {
        return devMode.dmDisplayFrequency;
    }

    return -1;
}
