/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <Windows.h>

char * swap_memory() {
    MEMORYSTATUSEX status;
    status.dwLength = sizeof(status);

    if (!GlobalMemoryStatusEx(&status)) {
        return NULL;
    }

    long long totalSwap = (long long)status.ullTotalPageFile;
    long long freeSwap = (long long)status.ullAvailPageFile;
    long long usedSwap = totalSwap - freeSwap;
    
    char buffer[128]; // Adjust the buffer size as needed

    // Use sprintf or snprintf to format the integers into the buffer
    snprintf(buffer, sizeof(buffer), "%lld,%lld,%lld", totalSwap, freeSwap, usedSwap);

    // Duplicate the buffer so that it can be returned from the function
    char * result = strdup(buffer);

    return result;
}
