/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <Windows.h>

#include "../../../../common/cpuid/const.h"
#include "../../../../common/regedit/registry.h"
#include "../../../../common/types/dict.h"

char * model() {
    char buffer[256];
    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "ProcessorNameString", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return buffer;
}

int logical_cores() {
    SYSTEM_INFO sysInfo;
    GetSystemInfo(&sysInfo);
    return sysInfo.dwNumberOfProcessors;
}

int physical_cores() {
    DWORD logicalProcessorCount = 0;
    DWORD physicalProcessorCount = 0;

    if (!GetLogicalProcessorInformation(NULL, &logicalProcessorCount)) {
        return -1; // Error
    }

    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION buffer = (PSYSTEM_LOGICAL_PROCESSOR_INFORMATION)malloc(logicalProcessorCount);

    if (!GetLogicalProcessorInformation(buffer, &logicalProcessorCount)) {
        free(buffer);
        return -1; // Error
    }

    DWORD byteOffset = 0;
    while (byteOffset + sizeof(SYSTEM_LOGICAL_PROCESSOR_INFORMATION) <= logicalProcessorCount) {
        PSYSTEM_LOGICAL_PROCESSOR_INFORMATION item = (PSYSTEM_LOGICAL_PROCESSOR_INFORMATION)((BYTE*)buffer + byteOffset);
        if (item->Relationship == RelationProcessorCore) {
            physicalProcessorCount++;
        }
        byteOffset += sizeof(SYSTEM_LOGICAL_PROCESSOR_INFORMATION);
    }

    free(buffer);
    return physicalProcessorCount;
}

char * architecture() {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment", "PROCESSOR_ARCHITECTURE", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return buffer;
}

int clockspeed() {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "~MHz", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return atoi(buffer);
}

char * vendor() {
    char buffer[256];

    int result = readRegistryValue(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "VendorIdentifier", buffer, sizeof(buffer));

    if (result != 0) {
        return NULL;
    }

    return buffer;
}

const char * manufacturer() {
    size_t dict_size = sizeof(vmap_manufacturer) / sizeof(vmap_manufacturer[0]);
    char * manufacturer = value_from_dict(vmap_manufacturer, dict_size, vendor(), "");
    return manufacturer;
}

const char * cpu_type() {
    size_t dict_size = sizeof(vmap_type) / sizeof(vmap_type[0]);
    char * cpu_type = value_from_dict(vmap_type, dict_size, vendor(), "");
    return cpu_type;
}
