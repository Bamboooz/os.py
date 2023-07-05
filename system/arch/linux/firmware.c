/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <unistd.h>

const char * firmware() {
    const int is_uefi = (access("/sys/firmware/efi", F_OK) == 0) ? 1 : 0;
    return is_uefi ? "UEFI" : "BIOS";
}
