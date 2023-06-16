/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <windows.h>

int percentage() {
    SYSTEM_POWER_STATUS powerStatus;
    if (GetSystemPowerStatus(&powerStatus))
    {
        if (powerStatus.BatteryLifePercent != BATTERY_PERCENTAGE_UNKNOWN)
        {
            return powerStatus.BatteryLifePercent;
        }

        return -1; // Failed to retrieve charge percentage
    }

    return -1; // Battery percentage retrieval failed
}

int charging() {
    SYSTEM_POWER_STATUS powerStatus;
    if (GetSystemPowerStatus(&powerStatus))
    {
        if (powerStatus.ACLineStatus == AC_LINE_ONLINE)
        {
            return 1; // Device is connected to a power source
        }
        else if (powerStatus.ACLineStatus == AC_LINE_OFFLINE)
        {
            return 0; // Device is not connected to a power source
        }

        return -1; // Failed to retrieve charge status
    }

    return -1; // Cannot determine if device is connected to a power source
}

int present() {
    SYSTEM_POWER_STATUS powerStatus;
    if (GetSystemPowerStatus(&powerStatus))
    {
        if (powerStatus.BatteryFlag & BATTERY_FLAG_NO_BATTERY)
        {
            return 0; // No system battery installed
        }

        return 1; // Found battery
    }

    return -1; // Battery information retrieval failed
}

int flag() {
    /*
    Value	Meaning
    1       High—the battery capacity is at more than 66 percent
    2       Low—the battery capacity is at less than 33 percent
    4       Critical—the battery capacity is at less than five percent
    8       Charging
    128     No system battery
    255     Unknown status—unable to read the battery flag information
    -1      Unknown status—unable to read the battery flag information
    */
    SYSTEM_POWER_STATUS powerStatus;
    if (GetSystemPowerStatus(&powerStatus))
    {
        return powerStatus.BatteryFlag;
    }

    return -1; // Battery information retrieval failed
}

int time() {
    SYSTEM_POWER_STATUS powerStatus;
    if (GetSystemPowerStatus(&powerStatus))
    {
        if (powerStatus.BatteryLifeTime != -1 && powerStatus.BatteryLifeTime != 0xFFFFFFFF)
        {
            return powerStatus.BatteryLifeTime / 60; // BatteryLifeTime is in seconds, convert to minutes
        }

        return -1; // Failed to retrieve battery time left
    }
    
    return -1; // Battery time left retrieval failed
}
