# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from collections import namedtuple

from _ospy_linux import *


def sensors_battery() -> namedtuple:
    """
    Returns a named tuple with system battery information.

    If multiple system batteries installed returns data from the one with the biggest success rate.

    If failed to retrieve particular data it will be set as None.

    Contains values:
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
    bat_stat_format = namedtuple('bat_stat_format', ['percentage', 'time_left', 'charging', 'flag', 'present'])

    if HAS_BATTERY is False:
        battery_status_no_battery_format = bat_stat_format(percentage=None, time_left=None, charging=None, flag=BATTERY_STATUS_NO_BATTERY, present=False)
        return battery_status_no_battery_format

    battery_status = _best_battery_status()

    percentage = battery_status['capacity']
    time_left = battery_status['time_left']
    is_charging = battery_status['status'] == 'charging'
    flag = _get_battery_flag(percentage, is_charging)

    battery_status_success_format = bat_stat_format(percentage=percentage, time_left=time_left, charging=is_charging, flag=flag, present=True)
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


def _best_battery_status() -> dict:
    """
    Load the battery information of each installed battery and return the one with the biggest retrieval success rate.
    """
    info_per_battery = {}

    for index, battery in enumerate(BATTERIES):
        info_per_battery[index] = _get_battery_status(battery)

    min_none_subdict = min(info_per_battery.values(), key=lambda subdict: sum(value is None for value in subdict.values()))

    return min_none_subdict  # Return the battery which had the most successful scan rate.


def _get_battery_status(battery: str):
    """
    Get battery status by battery name.
    """
    battery_info = {}

    # Try to read all required battery information.
    for bat_stat in ['capacity', 'status', 'energy_now', 'power_now']:
        try:
            with open(f'{POWER_SUPPLY_PATH}/{battery}/{bat_stat}', 'r') as file:
                battery_info[bat_stat] = file.read().strip().lower()
        except:
            # If failed set the value as None.
            battery_info[bat_stat] = None

    return _validate_battery_status(battery_info)


def _validate_battery_status(status) -> dict:
    """
    Convert all the values in the battery information to their go-to data types and calculate battery time left.
    """
    try:
        status['energy_now'] = int(status['energy_now'])
    except:
        status['energy_now'] = None

    try:
        status['power_now'] = int(status['power_now'])
    except:
        status['power_now'] = None

    try:
        status['capacity'] = int(status['capacity'])
    except:
        status['capacity'] = None

    try:
        if status['energy_now'] > 0 and status['power_now'] > 0:  # Calculate battery time left.
            status['time_left'] = status['energy_now'] / status['power_now'] * 60  # Convert to seconds
        else:
            status['time_left'] = None
    except:
        status['time_left'] = None

    return status
