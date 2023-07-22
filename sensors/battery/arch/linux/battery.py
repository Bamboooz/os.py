# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os

from common.data import ospylib_data_format

POWER_SUPPLY_PATH = "/sys/class/power_supply"

BATTERIES = [battery for battery in os.listdir(POWER_SUPPLY_PATH) if battery.startswith('BAT') or 'battery' in battery.lower()]
HAS_BATTERY = True if BATTERIES else False

BATTERY_STATUS_HIGH = 0
BATTERY_STATUS_MEDIUM = 1
BATTERY_STATUS_LOW = 2
BATTERY_STATUS_CRITICAL = 4
BATTERY_STATUS_CHARGING = 8
BATTERY_STATUS_NO_BATTERY = 128
BATTERY_STATUS_FAILED = 255

BATTERY_CAPACITY = 'capacity'
BATTERY_CHARGING = 'status'
BATTERY_TIME_LEFT = ['energy_now', 'power_now']


def sensors_battery() -> ospylib_data_format:
    """
    Returns a namedtuple-like with system battery information.

    If multiple system batteries installed returns data from the one with the biggest success rate.

    If failed to retrieve particular data it will be set as None.

    :returns:
        - percentage: Current battery percentage
        - time_left: Current estimated battery time left
        - present: Is any battery installed
        - charging: Is the device plugged in and charging
        - flag: Battery flag, see below

    Possible battery flags:
    Value	  Meaning
    0         High—the battery capacity is 66 percent or higher
    1         Medium—the battery percentage is higher or equal to 33 and lower than 66 percent
    2         Low—the battery percentage higher or equal to 5 and lower than 33 percent
    4         Critical—the battery percentage is at less than five percent
    8         Charging
    128       No system battery
    255       Unknown status—unable to read the battery flag information
    """
    battery_format = ospylib_data_format("sensors_battery", ["percentage", "time_left", "charging", "flag", "present"])

    if not HAS_BATTERY:
        return battery_format(percentage=None, time_left=None, charging=None, flag=BATTERY_STATUS_NO_BATTERY, present=False)

    battery_flag_format = battery_format(percentage=[_get_battery_status, [BATTERY_CAPACITY]], charging=[_get_battery_status, [BATTERY_CHARGING]])

    battery_status_success_format = battery_format(
        percentage=[_get_battery_status, [BATTERY_CAPACITY]],
        time_left=[_get_battery_status, [BATTERY_TIME_LEFT]],
        charging=[_get_battery_status, [BATTERY_CHARGING]],
        flag=[_get_battery_flag, [battery_flag_format.percentage, battery_flag_format.charging]],
        present=True
    )

    return battery_status_success_format


def _get_battery_flag(percentage, is_charging) -> int:
    """
    Possible battery flags:
    Value	  Meaning
    0         High—the battery capacity is 66 percent or higher
    1         Medium—the battery percentage is higher or equal to 33 and lower than 66 percent
    2         Low—the battery percentage higher or equal to 5 and lower than 33 percent
    4         Critical—the battery percentage is at less than five percent
    8         Charging
    128       No system battery
    255       Unknown status—unable to read the battery flag information

    Using a custom flag system as the default one makes literally no sense.
    It makes values 33 to 66 percent not be detected as any flag returning None.

    Don't have to implement the not found as it is covered directly in sensors_battery()
    """
    if is_charging is True:
        return BATTERY_STATUS_CHARGING

    if percentage is None:
        return BATTERY_STATUS_FAILED

    if percentage < 5:
        return BATTERY_STATUS_CRITICAL
    elif 5 <= percentage < 33:
        return BATTERY_STATUS_LOW
    elif 33 <= percentage < 66:
        return BATTERY_STATUS_MEDIUM
    elif percentage >= 66:
        return BATTERY_STATUS_HIGH


def _get_battery_status(data_type):
    data_info_per_batteries = {}

    for battery in BATTERIES:
        data_info = []

        if type(data_type) is not list:
            data_type = [data_type]

        for info in data_type:
            try:
                with open(f'{POWER_SUPPLY_PATH}/{battery}/{info}', 'r') as file:
                    data_info.append(file.read().strip().lower())
            except Exception:
                data_info.append(None)

        data_info_per_batteries[battery] = data_info

    best_battery_status = _best_battery_status(data_info_per_batteries)
    return _validate_battery_status(best_battery_status, data_type)


def _best_battery_status(status_dict: dict):
    for item in status_dict.values():
        if None not in item:
            return item


def _validate_battery_status(status, data_type):
    if not status:
        return None

    if BATTERY_CHARGING in data_type:
        return status[0].lower() == "charging"

    if BATTERY_CAPACITY in data_type:
        try:
            return int(status[0])
        except Exception:
            return None

    if BATTERY_TIME_LEFT in data_type:
        try:
            energy_now, power_now = (int(item) for item in status)
        except Exception:
            return None

        if energy_now > 0 and power_now > 0:  # Calculate battery time left.
            return energy_now / power_now * 60  # Convert to seconds
