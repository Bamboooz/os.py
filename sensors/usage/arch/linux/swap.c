/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double swap_percent() {
    FILE * meminfo = fopen("/proc/meminfo", "r");
    if (!meminfo) {
        return -1.0; // Error opening file
    }

    long total_swap = 0;
    long free_swap = 0;
    char line[128];

    while (fgets(line, sizeof(line), meminfo)) {
        if (strncmp(line, "SwapTotal:", 10) == 0) {
            total_swap = atol(line + 10);
        } else if (strncmp(line, "SwapFree:", 9) == 0) {
            free_swap = atol(line + 9);
        }
    }

    fclose(meminfo);

    if (total_swap <= 0 || free_swap <= 0) {
        return -1.0; // Invalid swap values
    }

    long used_swap = total_swap - free_swap;
    double swap_usage = ((double)used_swap / total_swap) * 100.0;

    return swap_usage;
}
