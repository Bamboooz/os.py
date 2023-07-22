/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stddef.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    char * key;
    char * value;
} dict;

char * value_from_dict(dict * dictionary, size_t dict_size, char * key, char * default_value) {
    for (size_t i = 0; i < dict_size; i++) {
        if (strcmp(dictionary[i].key, key) == 0) {
            return dictionary[i].value;
        }
    }

    return default_value;
}
