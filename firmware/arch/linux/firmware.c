/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * firmware() {
    int is_uefi = access("/sys/firmware/efi", F_OK);
    const char * firmware_type = is_uefi ? "UEFI" : "BIOS";
    return firmware_type;
}

char * version() {
    FILE * dmi_file = fopen("/sys/class/dmi/id/bios_version", "r");
    if (!dmi_file) {
        return NULL;
    }

    char version[128];
    fgets(version, sizeof(version), dmi_file);
    fclose(dmi_file);

    return version;
}

char * release_date() {
    FILE * dmi_file = fopen("/sys/class/dmi/id/bios_release", "r");
    if (!dmi_file) {
        return NULL;
    }

    char release_date[128];
    fgets(release_date, sizeof(release_date), dmi_file);
    fclose(dmi_file);

    return release_date;
}

char * vendor() {
    FILE * dmi_file = fopen("/sys/class/dmi/id/bios_vendor", "r");
    if (!dmi_file) {
        return NULL;
    }

    char vendor[128];
    fgets(vendor, sizeof(vendor), dmi_file);
    fclose(dmi_file);

    return vendor;
}
