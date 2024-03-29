/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <Windows.h>
#include <TlHelp32.h>
#include <unistd.h>

int getpid() {
    return GetCurrentProcessId();
}

int pid_exists(int pid) {
    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (snapshot == INVALID_HANDLE_VALUE) {
        return 0; // Failed to create snapshot
    }

    PROCESSENTRY32 processEntry;
    processEntry.dwSize = sizeof(PROCESSENTRY32);

    if (Process32First(snapshot, &processEntry)) {
        do {
            if (processEntry.th32ProcessID == (DWORD)pid) {
                CloseHandle(snapshot);
                return 1; // Process exists
            }
        } while (Process32Next(snapshot, &processEntry));
    }

    CloseHandle(snapshot);
    return 0; // Process does not exist
}
