/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>

typedef BOOL (WINAPI * PIsHvciEnabled)();

int uptime() {
    return (int)(GetTickCount() / 1000);
}

int safe_mode() {
    return (int)(GetSystemMetrics(SM_CLEANBOOT) != 0);
}

int hvci() {
    int hvciEnabled = 0;
    HMODULE kernel32 = GetModuleHandleA("kernel32.dll");
    if (kernel32) {
        FARPROC proc = GetProcAddress(kernel32, "IsHvciEnabled");
        PIsHvciEnabled pIsHvciEnabled = (PIsHvciEnabled)proc;
        hvciEnabled = (pIsHvciEnabled != NULL) ? pIsHvciEnabled() : 0;
    }
    return hvciEnabled;
}
