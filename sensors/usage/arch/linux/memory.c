/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double memory_percent() {
    FILE * meminfo = fopen("/proc/meminfo", "r");
    if (!meminfo) {
        return -1.0; // Error opening file
    }

    long total_memory = 0;
    long free_memory = 0;
    char line[128];

    while (fgets(line, sizeof(line), meminfo)) {
        if (strncmp(line, "MemTotal:", 9) == 0) {
            total_memory = atol(line + 9);
        } else if (strncmp(line, "MemFree:", 8) == 0) {
            free_memory = atol(line + 8);
        }
    }

    fclose(meminfo);

    if (total_memory <= 0 || free_memory <= 0) {
        return -1.0; // Invalid memory values
    }

    long used_memory = total_memory - free_memory;
    double memory_usage = ((double)used_memory / total_memory) * 100.0;

    return memory_usage;
}
