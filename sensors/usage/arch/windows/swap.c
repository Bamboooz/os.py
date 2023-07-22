/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>

double swap_percent() {
    MEMORYSTATUSEX status;
    status.dwLength = sizeof(status);

    if (!GlobalMemoryStatusEx(&status)) {
        return -1.0;
    }

    double totalSwap = (double)status.ullTotalPageFile;
    double usedSwap = totalSwap - (double)status.ullAvailPageFile; // used = total - free swap
    double swapUsage = (usedSwap / totalSwap) * 100.0;

    return swapUsage;
}
