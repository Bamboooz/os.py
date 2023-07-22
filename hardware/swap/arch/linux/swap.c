/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * swap_memory() {
    FILE * meminfo = fopen("/proc/meminfo", "r");
    if (!meminfo) {
        return NULL;
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

    if (total_swap <= 0 || free_swap < 0) {
        return NULL;
    }

    long used_swap = total_swap - free_swap;

    long long total_swap_bytes = total_swap * 1024;
    long long used_swap_bytes = used_swap * 1024;
    long long free_swap_bytes = free_swap * 1024;

    char buffer[128]; // Adjust the buffer size as needed

    // Use sprintf or snprintf to format the integers into the buffer
    snprintf(buffer, sizeof(buffer), "%lld,%lld,%lld", total_swap_bytes, used_swap_bytes, free_swap_bytes);

    // Duplicate the buffer so that it can be returned from the function
    return strdup(buffer);
}
