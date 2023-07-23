/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>

char * filesystem(const char * drive_path) {
    char volume_name_buffer[MAX_PATH];
    char file_system_name_buffer[MAX_PATH];
    ULONG max_component_length = 0;
    ULONG file_system_flags = 0;

    if (!GetVolumeInformationA(drive_path,
                               volume_name_buffer,
                               MAX_PATH,
                               NULL,
                               &max_component_length,
                               &file_system_flags,
                               file_system_name_buffer,
                               MAX_PATH)) {
        return NULL; // Failed to get volume information
    }

    return strdup(file_system_name_buffer);
}
