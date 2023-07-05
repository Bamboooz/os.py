/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>

int total() {
    FILE * file = fopen("/proc/meminfo", "r");
    if (file == NULL) {
        return -1;
    }

    char line[256];
    int totalSwapMemory = 0;
    while (fgets(line, sizeof(line), file)) {
        if (sscanf(line, "SwapTotal: %*u kB") == 0) {
            if (sscanf(line, "SwapTotal: %d kB", &totalSwapMemory) == 1) {
                break;
            }
        }
    }

    fclose(file);
    return totalSwapMemory * 1024;  // Convert kilobytes to bytes
}
