/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <Windows.h>
#include <stdbool.h>
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SYSTEM_INFORMATION_BUFFER 256
#define LANG_BUFFER_SIZE 256

const char * hostname() {
    static char hostname[SYSTEM_INFORMATION_BUFFER];
    DWORD length = sizeof(hostname);
    
    if (!GetComputerNameA(hostname, &length)) {
        return NULL;
    }

    return hostname;
}

const char * version() {
    OSVERSIONINFOEX osvi;
    ZeroMemory(&osvi, sizeof(OSVERSIONINFOEX));
    osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);

    if (GetVersionEx((OSVERSIONINFO*)&osvi) == 0) {
        return NULL;
    }

    static char version[SYSTEM_INFORMATION_BUFFER];
    snprintf(version, sizeof(version), "%d.%d.%d", osvi.dwMajorVersion, osvi.dwMinorVersion, osvi.dwBuildNumber);
    return version;
}

const char * platform() {
    OSVERSIONINFOEX osvi;
    ZeroMemory(&osvi, sizeof(OSVERSIONINFOEX));
    osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);

    if (GetVersionEx((OSVERSIONINFO*)&osvi) == 0) {
        return NULL;
    }

    char release[128];
    snprintf(release, sizeof(release), "%d.%d.%d", osvi.dwMajorVersion, osvi.dwMinorVersion, osvi.dwBuildNumber);

    char machine[SYSTEM_INFORMATION_BUFFER];
    DWORD machineSize = sizeof(machine);
    if (GetEnvironmentVariable("PROCESSOR_ARCHITECTURE", machine, machineSize) == 0) {
        return NULL;
    }

    static char platform[SYSTEM_INFORMATION_BUFFER];
    snprintf(platform, sizeof(platform), "Windows-%s-%s", release, machine);
    return platform;
}

const char * release() {
    OSVERSIONINFOEX osvi;
    ZeroMemory(&osvi, sizeof(OSVERSIONINFOEX));
    osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);

    if (GetVersionEx((OSVERSIONINFO*)&osvi) == 0) {
        return NULL;
    }

    static char result[SYSTEM_INFORMATION_BUFFER];
    snprintf(result, sizeof(result), "%d.%d.%d", osvi.dwMajorVersion, osvi.dwMinorVersion, osvi.dwBuildNumber);
    return result;
}

const char * arch() {
    static char machine[SYSTEM_INFORMATION_BUFFER];
    DWORD machineSize = sizeof(machine);

    if (GetEnvironmentVariable("PROCESSOR_ARCHITECTURE", machine, machineSize) == 0) {
        return NULL;
    }

    return machine;
}

const char * user() {
    const char * username = getenv("USERNAME");
    
    BOOL isAdmin = FALSE;
    SID_IDENTIFIER_AUTHORITY ntAuthority = SECURITY_NT_AUTHORITY;
    PSID administratorsGroup;

    if (AllocateAndInitializeSid(&ntAuthority, 2, SECURITY_BUILTIN_DOMAIN_RID, DOMAIN_ALIAS_RID_ADMINS, 0, 0, 0, 0, 0, 0, &administratorsGroup)) {
        if (!CheckTokenMembership(NULL, administratorsGroup, &isAdmin)) {
            isAdmin = FALSE;
        }
        FreeSid(administratorsGroup);
    }

    static char buffer[SYSTEM_INFORMATION_BUFFER];
    snprintf(buffer, sizeof(buffer), "(%s,%s)", username, isAdmin ? "True" : "False");
    return buffer;
}

const char * lang() {
    setlocale(LC_ALL, "");
    static char lang_env[LANG_BUFFER_SIZE];
    char * env = getenv("LANG");
    if (env == NULL) {
        return NULL;
    }
    snprintf(lang_env, LANG_BUFFER_SIZE, "%s", env);
    char * dot = strchr(lang_env, '.');
    if (dot != NULL) {
        *dot = '\0';
    }

    UINT codePage = GetACP();
    static char encoding[32];
    snprintf(encoding, sizeof(encoding), "cp%d", codePage);

    static char buffer[SYSTEM_INFORMATION_BUFFER];
    snprintf(buffer, sizeof(buffer), "(%s,%s)", lang_env, encoding);
    return buffer;
}

int uptime() {
    DWORD ticks = GetTickCount();
    int seconds = ticks / 1000;
    return seconds;
}

int safe_mode() {
    int inSafeMode = GetSystemMetrics(SM_CLEANBOOT) != 0;
    return inSafeMode;
}

int hvci() {
    int hvciEnabled = 0;
    HMODULE kernel32 = GetModuleHandleA("kernel32.dll");
    typedef BOOL (WINAPI * PIsHvciEnabled)();

    if (kernel32) {
        FARPROC proc = GetProcAddress(kernel32, "IsHvciEnabled");
        PIsHvciEnabled pIsHvciEnabled = (PIsHvciEnabled)proc;
        hvciEnabled = (pIsHvciEnabled != NULL) ? pIsHvciEnabled() : 0;
    }
    
    return hvciEnabled ? 1 : 0;
}
