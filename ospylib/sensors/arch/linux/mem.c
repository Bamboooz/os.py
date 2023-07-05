/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>

double usage() {
    FILE * file = fopen("/proc/meminfo", "r");
    
    if (file == NULL) {
        return -1.0;
    }

    char line[256];
    unsigned long long total_memory = 0;
    unsigned long long free_memory = 0;
    unsigned long long used_memory = 0;

    while (fgets(line, sizeof(line), file)) {
        if (sscanf(line, "MemTotal: %llu", &total_memory) == 1) {
            // Convert total memory to kilobytes
            total_memory /= 1024;
        } else if (sscanf(line, "MemFree: %llu", &free_memory) == 1) {
            // Convert free memory to kilobytes
            free_memory /= 1024;
        }
    }

    fclose(file);

    used_memory = total_memory - free_memory;

    double usage_percentage = (double)used_memory / total_memory * 100.0;

    return usage_percentage;
}
