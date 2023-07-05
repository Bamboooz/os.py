/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <windows.h>

#include "../../../common/cpuid/types.h"
#include "../../../common/regedit/registry.c"
#include "../../../common/strlib.h"

const char * model() {
    char * model = read_registry_value(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "ProcessorNameString");
    return trim(model);
}

const int cores() {
    int subkeys = count_subkeys(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor");
    return subkeys;
}

const char * architecture() {
    char * architecture = read_registry_value(HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment", "PROCESSOR_ARCHITECTURE");
    return trim(architecture);
}

const int clockspeed() {
    char * clockspeed = read_registry_value(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "~MHz");
    return atoi(trim(clockspeed));
}

const char * vendor() {
    char * vendor = read_registry_value(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "VendorIdentifier");
    return vendor;
}

const char * manufacturer() {
    for (size_t i = 0; i < sizeof(vmap) / sizeof(vmap[0]); i++) {
        if (strcmp(vendor(), vmap[i].id) == 0) {
            return vmap[i].manufacturer;
        }
    }
    return "Unknown";
}

const char * cpu_type() {
    for (size_t i = 0; i < sizeof(vmap) / sizeof(vmap[0]); i++) {
        if (strcmp(vendor(), vmap[i].id) == 0) {
            return vmap[i].type;
        }
    }
    return "Unknown";
}

int main() {
    printf("%s\n", vendor());
    printf("%s\n", manufacturer());
}