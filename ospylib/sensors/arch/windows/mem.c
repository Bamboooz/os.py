#include <windows.h>
#include <stdio.h>

double mem_usage() {
    MEMORYSTATUS status;
    GlobalMemoryStatus(&status);

    DWORDLONG totalPhysicalMemory = status.dwTotalPhys;
    DWORDLONG availablePhysicalMemory = status.dwAvailPhys;

    double memoryUsage = 100.0 - ((double)availablePhysicalMemory / (double)totalPhysicalMemory) * 100.0;
    return memoryUsage;
}

double mem_usage_per_stick() {
    return 0.0;
}
