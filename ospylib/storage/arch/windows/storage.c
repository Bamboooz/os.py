/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>

const char * g_root(const char * drive) {
    /*
    Converts drive letters to root paths ("C" -> "C:\", "C:\" -> "C:\") etc.
    */
    static char rootPath[MAX_PATH];
    strncpy(rootPath, drive, sizeof(rootPath));

    char * lastChar = &rootPath[strlen(rootPath) - 1];
    if (* lastChar != '\\' && * lastChar != '/') {
        strcat(rootPath, "\\");
    }

    return rootPath;
}

char * drives() {
    /*
    Returns a dynamically allocated string containing a list of installed drives (C:\\, D:\\) etc.
    */
    char buffer[256];
    DWORD drivesLength = GetLogicalDriveStringsA(sizeof(buffer), buffer);
    char * drive = buffer;

    // Calculate the total length needed for the string
    size_t totalLength = 0;
    while (* drive) {
        totalLength += strlen(drive) + 1;  // +1 for newline character
        drive += strlen(drive) + 1;
    }

    // Allocate memory for the string
    char* driveList = (char*)malloc(totalLength);
    if (driveList == NULL) {
        return NULL;  // Failed to allocate memory
    }

    // Construct the drive list string
    drive = buffer;
    char * driveListPtr = driveList;
    while (* drive) {
        strcpy(driveListPtr, drive);
        driveListPtr += strlen(drive);
        * driveListPtr = '\n';
        driveListPtr++;
        drive += strlen(drive) + 1;
    }

    // Null-terminate the string
    *driveListPtr = '\0';

    return driveList;
}

double s_total(const char * drive) {
    /*
    Returns the total space of an installed drive in bytes.

    Returns -1.0 if it fails to retrieve the data or the drive doesn't exist.
    */
    ULARGE_INTEGER totalSpace;
    const char * rootPath = g_root(drive);

    if (!GetDiskFreeSpaceExA(rootPath, NULL, &totalSpace, NULL)) {
        return -1.0;
    }

    return (double)totalSpace.QuadPart;
}

double s_used(const char * drive) {
    /*
    Returns the used space of an installed drive in bytes.

    Returns -1.0 if it fails to retrieve the data or the drive doesn't exist.
    */
    ULARGE_INTEGER totalSpace;
    ULARGE_INTEGER freeSpace;
    const char * rootPath = g_root(drive);

    if (!GetDiskFreeSpaceExA(rootPath, &freeSpace, &totalSpace, NULL)) {
        return -1.0;
    }

    return (double)(totalSpace.QuadPart - freeSpace.QuadPart);
}

double s_free(const char * drive) {
    /*
    Returns the free space of an installed drive in bytes.

    Returns -1.0 if it fails to retrieve the data or the drive doesn't exist.
    */
    ULARGE_INTEGER totalSpace;
    const char * rootPath = g_root(drive);

    if (!GetDiskFreeSpaceExA(rootPath, &totalSpace, NULL, NULL)) {
        return -1.0;
    }

    return (double)totalSpace.QuadPart;
}

double p_free(const char * drive) {
    /*
    Returns the percentage of free space of an installed drive.

    Returns -1.0 if it fails to retrieve the data or the drive doesn't exist.
    */
    double totalSpace = s_total(drive);
    double freeSpace = s_free(drive);
    double freeSpacePercent = (freeSpace / totalSpace) * 100.0;

    if (freeSpace == -1.0 || totalSpace == -1.0) {
        freeSpacePercent = -1.0;
    }

    return freeSpacePercent;
}

double p_used(const char * drive) {
    /*
    Returns the percentage of used space of an installed drive.

    Returns -1.0 if it fails to retrieve the data or the drive doesn't exist.
    */
    double totalSpace = s_total(drive);
    double usedSpace = s_used(drive);
    double usedSpacePercent = (usedSpace / totalSpace) * 100.0;

    if (usedSpace == -1.0 || totalSpace == -1.0) {
        usedSpacePercent = -1.0;
    }

    return usedSpacePercent;
}
