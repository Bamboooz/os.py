/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>

#include "../../../common/regedit/registry.c"

#define USER_PERMISSION_ADMINISTRATOR 1
#define USER_PERMISSION_NORMAL 0

typedef BOOL (WINAPI * PIsHvciEnabled)();

int admin() {
    BOOL isAdmin = FALSE;
    SID_IDENTIFIER_AUTHORITY NtAuthority = SECURITY_NT_AUTHORITY;
    PSID AdministratorsGroup;

    if (AllocateAndInitializeSid(&NtAuthority, 2, SECURITY_BUILTIN_DOMAIN_RID, DOMAIN_ALIAS_RID_ADMINS, 0, 0, 0, 0, 0, 0, &AdministratorsGroup)) {
        if (!CheckTokenMembership(NULL, AdministratorsGroup, &isAdmin)) {
            isAdmin = FALSE;
        }
        FreeSid(AdministratorsGroup);
    }
    
    return isAdmin;
}

int uptime() {
    return (int)(GetTickCount() / 1000);
}

int safeMode() {
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
