/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <windows.h>
#include <stdio.h>

double usage() {
    MEMORYSTATUS status;
    GlobalMemoryStatus(&status);

    DWORDLONG totalPhysicalMemory = status.dwTotalPhys;
    DWORDLONG availablePhysicalMemory = status.dwAvailPhys;

    double memoryUsage = 100.0 - ((double)availablePhysicalMemory / (double)totalPhysicalMemory) * 100.0;
    return memoryUsage;
}
