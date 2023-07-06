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

    Possible battery flags:
    Value	  Meaning
    1         High—the battery capacity is at more than 66 percent
    2         Low—the battery capacity is at less than 33 percent
    4         Critical—the battery capacity is at less than five percent
    8         Charging
    128       No system battery
    255       Unknown status—unable to read the battery flag information
    """
    bat_stat_format = namedtuple('bat_stat_format', ['percentage', 'time_left', 'charging', 'flag', 'present'])

    if HAS_BATTERY is False:
        battery_status_no_battery_format = bat_stat_format(percentage=None, time_left=None, charging=None, flag=BATTERY_STATUS_NO_BATTERY, present=False)
        return battery_status_no_battery_format

    battery_status = _battery_status()

    percentage = battery_status['capacity']
    time_left = battery_status['time_left']
    is_charging = battery_status['status'] == 'charging'
    flag = _get_battery_flag(percentage, is_charging)

    battery_status_success_format = bat_stat_format(percentage=percentage, time_left=time_left, charging=is_charging, flag=flag, present=True)
    return battery_status_success_format


def _get_battery_flag(percentage, is_charging):
    # Value	  Meaning
    # 1       High—the battery capacity is at more than 66 percent
    # 2       Low—the battery capacity is at less than 33 percent
    # 4       Critical—the battery capacity is at less than five percent
    # 8       Charging
    # 128     No system battery
    # 255     Unknown status—unable to read the battery flag information

    # Don't have to implement the not found as it is covered directly in sensors_battery()

    if is_charging is None or percentage is None:
        return BATTERY_STATUS_FAILED

    if is_charging is True:
        return BATTERY_STATUS_CHARGING

    if percentage < 5:
        return BATTERY_STATUS_CRITICAL
    elif percentage < 33:
        return BATTERY_STATUS_LOW
    elif percentage > 66:
        return BATTERY_STATUS_HIGH


def _battery_status():
    info_per_battery = {}

    # Iterate over all batteries, return the one with the biggest success rate.
    for battery_index, battery in enumerate(BATTERIES):
        battery_info = {}

        # Try to read all required battery information.
        for data_index, bat_stat in enumerate(['capacity', 'status', 'energy_now', 'power_now']):
            try:
                with open(f'{POWER_SUPPLY_PATH}/{battery}/{bat_stat}', 'r') as file:
                    battery_info[bat_stat] = file.read().strip().lower()
            except:
                # If failed set the value as None.
                battery_info[bat_stat] = None

        # Check if the values in the extracted files are correct.
        try:
            battery_info['energy_now'] = int(battery_info['energy_now'])
        except:
            battery_info['energy_now'] = None

        try:
            battery_info['power_now'] = int(battery_info['power_now'])
        except:
            battery_info['power_now'] = None

        try:
            battery_info['capacity'] = int(battery_info['capacity'])
        except:
            battery_info['capacity'] = None

        # Calculate battery time left.
        if battery_info['energy_now'] is not None and battery_info['power_now'] is not None and battery_info['energy_now'] > 0 and battery_info['power_now'] > 0:
            battery_info['time_left'] = battery_info['energy_now'] / battery_info['power_now'] * 60  # Convert to seconds
        else:
            battery_info['time_left'] = None

        info_per_battery[battery_index] = battery_info

    min_none_count = float('inf')
    min_none_subdict = None

    # Iterate over all the batteries and find the one with the least None values.
    for key, subdict in info_per_battery.items():
        none_count = sum(value is None for value in subdict.values())
        if none_count < min_none_count:
            min_none_count = none_count
            min_none_subdict = subdict

    return min_none_subdict  # Return the battery which had the most successful scan rate.
