/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * layout() {
    FILE * file = fopen("/etc/default/keyboard", "r");
    if (file == NULL) {
        return NULL; // Error opening file
    }

    char line[256];
    char * layout_value = NULL;

    while (fgets(line, sizeof(line), file)) {
        if (strncmp(line, "XKBLAYOUT", 9) == 0) {
            char *layout = strchr(line, '=');
            if (layout) {
                layout++; // Move to the value part after '='
                while (*layout == ' ' || *layout == '\t' || *layout == '"') {
                    layout++; // Skip whitespace and quotation marks
                }
                // Remove the trailing newline character
                char *newline = strchr(layout, '\n');
                if (newline) {
                    *newline = '\0';
                }
                // Remove trailing quotation marks, if any
                char *end = strchr(layout, '"');
                if (end) {
                    *end = '\0';
                }
                layout_value = strdup(layout); // Duplicate the layout value
                break;
            }
        }
    }

    fclose(file);
    return layout_value;
}
