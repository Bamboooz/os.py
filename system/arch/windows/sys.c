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

int is_vm()
{
    HKEY hKey;

    char * buffer = read_registry_value(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System", "SystemBiosVersion");
    if (buffer == NULL)
    {
        return 0; // Failed to read the registry value
    }

    // Check if the value contains known VM strings
    const char * vmStrings[] = {
        "QEMU",
        "KVM",
        "VMware",
        "VirtualBox",
        "Xen",
        "Hyper-V",
        "Parallels",
        "bhyve",
        "QNX",
        "CPU",
        "Hypervisor"
    };

    int isVM = 0;
    for (size_t i = 0; i < sizeof(vmStrings) / sizeof(vmStrings[0]); i++)
    {
        if (strstr(buffer, vmStrings[i]) != NULL)
        {
            isVM = 1; // Found a match, indicating a virtual machine
            break;
        }
    }

    free(buffer);
    return isVM;
}
