/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>

double memory_percent() {
    MEMORYSTATUSEX status;
    status.dwLength = sizeof(status);

    if (!GlobalMemoryStatusEx(&status)) {
        return -1.0;
    }

    double totalMemory = (double)status.ullTotalPhys;
    double usedMemory = totalMemory - (double)status.ullAvailPhys; // used = total - free memory
    double memoryUsage = (usedMemory / totalMemory) * 100.0;

    return memoryUsage;
}
