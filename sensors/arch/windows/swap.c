/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <windows.h>

double usage() {
    MEMORYSTATUSEX status;
    status.dwLength = sizeof(status);
    GlobalMemoryStatusEx(&status);

    DWORDLONG totalSwap = status.ullTotalPageFile;
    DWORDLONG availableSwap = status.ullAvailPageFile;

    double swapUsage = 100.0 - ((double)availableSwap / (double)totalSwap) * 100.0;
    return swapUsage;
}
