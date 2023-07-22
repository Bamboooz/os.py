/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/utsname.h>

#include "../../../../common/cpuid/const.h"
#include "../../../../common/types/dict.h"

#define MAX_BUFFER_SIZE 1024

double ceil(double x) {
    // no idea why my compiler didn't detect math.ceil() so I made my own.
    if (x > (int)x) {
        x = (int)x + 1;
    }
    return x;
}

void read_file(const char * file_path, char * buffer, size_t buffer_size) {
    FILE * file = fopen(file_path, "r");

    size_t num_bytes_read = fread(buffer, sizeof(char), buffer_size - 1, file);
    buffer[num_bytes_read] = '\0';

    fclose(file);
}

char * proc_value(const char * cpuinfo, const char * keyword) {
    char * pos = strstr(cpuinfo, keyword);
    if (pos != NULL) {
        pos = strchr(pos, ':');
        if (pos != NULL) {
            pos += 2; // Skip the ':' and the space after it
            char * newline_pos = strchr(pos, '\n');
            if (newline_pos != NULL) {
                *newline_pos = '\0'; // Replace the newline with a null terminator
                return pos;
            }
        }
    }

    return NULL;
}

const char * model() {
    char cpuinfo[MAX_BUFFER_SIZE];
    read_file("/proc/cpuinfo", cpuinfo, sizeof(cpuinfo));
    return proc_value(cpuinfo, "model name");
}

int physical_cores() {
    char cpuinfo[MAX_BUFFER_SIZE];
    read_file("/proc/cpuinfo", cpuinfo, sizeof(cpuinfo));

    int num_processors = 0;
    char * processor_pos = strstr(cpuinfo, "physical id");
    while (processor_pos != NULL) {
        num_processors++;
        processor_pos = strstr(processor_pos + 1, "physical id");
    }

    return num_processors;
}

int logical_cores() {
    char cpuinfo[MAX_BUFFER_SIZE];
    read_file("/proc/cpuinfo", cpuinfo, sizeof(cpuinfo));

    int num_processors = 0;
    char * processor_pos = strstr(cpuinfo, "processor");
    while (processor_pos != NULL) {
        num_processors++;
        processor_pos = strstr(processor_pos + 1, "processor");
    }

    return num_processors;
}

const char * vendor() {
    char cpuinfo[MAX_BUFFER_SIZE];
    read_file("/proc/cpuinfo", cpuinfo, sizeof(cpuinfo));
    return proc_value(cpuinfo, "vendor_id");
}

int clockspeed() {
    char cpuinfo[MAX_BUFFER_SIZE];
    read_file("/proc/cpuinfo", cpuinfo, sizeof(cpuinfo));
    char * clock_speed_str = proc_value(cpuinfo, "cpu MHz");
    if (clock_speed_str != NULL) {
        double clock_speed = atof(clock_speed_str);
        return (int)ceil(clock_speed);
    }

    return 0;
}

const char * architecture() {
    struct utsname buffer;
    if (uname(&buffer) == 0) {
        static char architecture[MAX_BUFFER_SIZE];
        strncpy(architecture, buffer.machine, sizeof(architecture));
        architecture[sizeof(architecture) - 1] = '\0';
        return architecture;
    }

    return "";
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
