/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <unistd.h>
#include <stdio.h>

int getpid() {
    return getpid();
}

int pid_exists(int pid) {
    char path[64];
    snprintf(path, sizeof(path), "/proc/%d", pid);
    
    if (access(path, F_OK) == 0) {
        return 1;
    }
    
    return 0;
}
