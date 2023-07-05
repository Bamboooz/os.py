/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <windows.h>

#include "../../../common/regedit/registry.c"
#include "../../../common/strlib.h"

const char * product(){
    char * b_product = read_registry_value(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardProduct");
    return trim(b_product);
}

const char * manufacturer() {
    char * b_manufacturer = read_registry_value(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardManufacturer");
    return trim(b_manufacturer);
}

const char * version() {
    char * b_version = read_registry_value(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS", "BaseBoardVersion");
    return trim(b_version);
}
