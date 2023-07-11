/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>

typedef BOOL (WINAPI * PIsHvciEnabled)();

int is_admin() {
    BOOL isAdmin = FALSE;
    SID_IDENTIFIER_AUTHORITY ntAuthority = SECURITY_NT_AUTHORITY;
    PSID administratorsGroup;

    if (AllocateAndInitializeSid(&ntAuthority, 2, SECURITY_BUILTIN_DOMAIN_RID, DOMAIN_ALIAS_RID_ADMINS, 0, 0, 0, 0, 0, 0, &administratorsGroup)) {
        if (!CheckTokenMembership(NULL, administratorsGroup, &isAdmin)) {
            isAdmin = FALSE;
        }
        FreeSid(administratorsGroup);
    }

    return isAdmin;
}

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
