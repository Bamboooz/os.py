#include <stdio.h>
#include <Windows.h>
#include <TlHelp32.h>
#include <unistd.h>

int current_pid() {
    return getpid();
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
