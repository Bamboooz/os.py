/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define USER_PERMISSION_ADMINISTRATOR 1
#define USER_PERMISSION_NORMAL 0

int admin() {
    return (getuid() == 0);
}

int uptime() {
    FILE * file = fopen("/proc/uptime", "r");
    if (!file) {
        return -1;  // Error occurred
    }

    double uptimeValue;
    if (fscanf(file, "%lf", &uptimeValue) != 1) {
        fclose(file);
        return -1;  // Error occurred
    }

    fclose(file);
    return (int)uptimeValue;
}
