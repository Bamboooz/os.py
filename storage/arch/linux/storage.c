/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * filesystem(const char * mount_point) {
    char command[1024];
    snprintf(command, sizeof(command), "df -T %s", mount_point);

    FILE * fp = popen(command, "r");
    if (fp == NULL) {
        return NULL;
    }

    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    // Skip the first line containing headers
    if ((read = getline(&line, &len, fp)) == -1) {
        free(line);
        pclose(fp);
        return NULL;
    }

    char * filesystem = NULL;

    // Read the second line containing filesystem information
    if ((read = getline(&line, &len, fp)) != -1) {
        char * token = strtok(line, " \t\n");
        int count = 0;

        while (token != NULL) {
            if (count == 1) {
                filesystem = strdup(token);
                break;
            }
            token = strtok(NULL, " \t\n");
            count++;
        }
    }

    free(line);
    pclose(fp);
    return filesystem;
}
