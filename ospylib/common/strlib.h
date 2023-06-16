/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * trim(char * s) {
    char * start = s;
    char * end = s + strlen(s) - 1;

    // Trim leading spaces
    while (isspace((unsigned char) * start)) {
      start++;
    }

    // Trim trailing spaces
    while (end > start && isspace((unsigned char) * end)) {
      end--;
    }

    // Shift the trimmed string to the beginning
    size_t trimmed_length = end - start + 1;
    memmove(s, start, trimmed_length);
    s[trimmed_length] = '\0';

    return s;
}
