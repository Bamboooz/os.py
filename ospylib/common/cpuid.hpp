/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>
#include <cpuid.h>

const bool has_cpuid() {
    unsigned int eax, ebx, ecx, edx;

    if (__get_cpuid(0x80000000, &eax, &ebx, &ecx, &edx) && (eax >= 0x80000004)) {
        return true;
    } else {
        return false;
    }
}
