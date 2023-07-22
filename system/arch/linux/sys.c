/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <locale.h>
#include <sys/utsname.h>

#define SYSTEM_INFORMATION_BUFFER 256

const char * hostname() {
    static char hostname[SYSTEM_INFORMATION_BUFFER];

    if (gethostname(hostname, sizeof(hostname)) != 0) {
        return NULL;
    }

    return hostname;
}

const char * version() {
    struct utsname info;

    if (uname(&info) != 0) {
        return NULL;
    }

    static char version[SYSTEM_INFORMATION_BUFFER];
    snprintf(version, sizeof(version), "%s", info.version);
    return version;
}

const char * platform() {
    struct utsname info;

    if (uname(&info) != 0) {
        return NULL;
    }

    static char platform[SYSTEM_INFORMATION_BUFFER];
    snprintf(platform, sizeof(platform), "%s-%s-%s", info.sysname, info.release, info.machine);
    return platform;
}

const char * release() {
    struct utsname info;

    if (uname(&info) != 0) {
        return NULL;
    }

    static char release[SYSTEM_INFORMATION_BUFFER];
    snprintf(release, sizeof(release), "%s", info.release);
    return release;
}

const char * arch() {
    struct utsname info;

    if (uname(&info) != 0) {
        return NULL;
    }

    static char machine[SYSTEM_INFORMATION_BUFFER];
    snprintf(machine, sizeof(machine), "%s", info.machine);
    return machine;
}

const char * user() {
    char * username = getenv("USERNAME");
    int isAdmin = geteuid() == 0;

    static char user_info[SYSTEM_INFORMATION_BUFFER];
    snprintf(user_info, sizeof(user_info), "(%s, %s)", username, isAdmin ? "True" : "False");
    return user_info;
}

const char * lang() {
    setlocale(LC_ALL, "");
    char * lang_env = getenv("LANG");
    char * encoding = NULL;

    if (lang_env != NULL) {
        char * dot = strchr(lang_env, '.');
        if (dot != NULL) {
            *dot = '\0';
            encoding = dot + 1;
        }
    }

    static char lang_info[SYSTEM_INFORMATION_BUFFER];
    snprintf(lang_info, sizeof(lang_info), "(%s, %s)", lang_env, encoding);
    return lang_info;
}

int uptime() {
    FILE * file = fopen("/proc/uptime", "r");

    if (!file) {
        return -1;
    }

    int uptimeValue = 0;
    
    if (fscanf(file, "%i", &uptimeValue) != 1) {
        fclose(file);
        return -1;
    }

    fclose(file);
    return uptimeValue;
}
