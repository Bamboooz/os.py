/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>

#include "const.h"

void executeCpuid(unsigned int cpuidResults[4], unsigned int eaxValue, unsigned int ecxValue) {
    __asm__ volatile (
        "cpuid"
        : "=a" (cpuidResults[0]),
          "=b" (cpuidResults[1]),
          "=c" (cpuidResults[2]),
          "=d" (cpuidResults[3])
        : "a" (eaxValue),
          "c" (ecxValue)
    );
}

int cpuid_supported() {
    unsigned int cpuidResults[4];
    
    executeCpuid(cpuidResults, ECX, ECX);

    // Check if the CPUID instruction is supported
    return (cpuidResults[0] >= ECX);
}
