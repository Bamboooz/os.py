/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include "../../../hardware/arch/linux/processor.c"

double usage() {
    return 0.0;
}

double usage_of_core(int core) {
    int total_cores = cores(0) + cores(1);
    if (core > total_cores || core < 0) {
        return -1.0;
    }
}

double temp() {
    return 0.0;
}
