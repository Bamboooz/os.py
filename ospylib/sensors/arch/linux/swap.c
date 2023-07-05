/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>

double usage() {
    FILE * meminfo = fopen("/proc/meminfo", "r");

    if (meminfo == NULL) {
        return -1.0;
    }

    char buffer[256];
    long totalSwap = 0;
    long freeSwap = 0;

    while (fgets(buffer, sizeof(buffer), meminfo)) {
        sscanf(buffer, "SwapTotal: %ld kB", &totalSwap);
        sscanf(buffer, "SwapFree: %ld kB", &freeSwap);
    }

    fclose(meminfo);

    if (totalSwap > 0 && freeSwap > 0) {
        double swapUsed = 100.0 - ((double)freeSwap / totalSwap) * 100.0;
        return swapUsed;
    }

    return -1.0;
}
