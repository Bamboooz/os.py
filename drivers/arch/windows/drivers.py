# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.prompt.prompt import execute_command

from collections import namedtuple

DRIVER_QUERY_COMMAND = "driverquery /fo csv /v /nh"


def driver_query(driver: str=None) -> namedtuple or dict:
    """
    Returns a dict of drivers and information about them if driver not specified.
    {
        '<driver_name>': '<file_path>',
        ...
    }

    If driver name or driver path is specified, returns a named tuple with items:
        - name: Driver name
        - path: Path to the driver file
        - signed: Is driver signed
        - description: Drivers description
    """
    driver_data = _get_driver_data()
    drivers = list(driver_data.keys())
    driver_paths = [value[2] for value in driver_data.values()]

    if driver is None and driver_data is not None: return {key: value[2] for key, value in driver_data.items()}

    driver_data_format = namedtuple('driver_data_format', ['signed', 'path', 'name', 'description'])

    if driver in drivers: return _get_data_from_name(driver, driver_data)

    if driver in driver_paths: return _get_data_from_path(driver, driver_data)

    driver_not_found = driver_data_format(signed=None, path=None, name=None, description=None)
    return driver_not_found


def _get_driver_data() -> dict or None:
    """
    Get driver information from command prompt.
    """
    try:
        output = execute_command(DRIVER_QUERY_COMMAND, trim=0, encodings=['cp1252'])
    except:
        return None

    driver_locations = {
        # |   driver name   | | driver description | |          is driver signed          |  |  driver file path  |
        values[0].strip('"'): [values[1].strip('"'), values[7].strip('"').lower() == 'true', values[-2].strip('"')]
        for values in (line.split(',') for line in output)
    }

    return driver_locations


def _get_data_from_name(driver: str, driver_data: dict) -> namedtuple:
    """
    Get driver information from driver name.
    """
    driver_data_format = namedtuple('driver_data_format', ['signed', 'path', 'name', 'description'])

    description = driver_data[driver][0]
    signed = driver_data[driver][1]
    file_path = driver_data[driver][2]

    return driver_data_format(signed=signed, description=description, path=file_path, name=driver)


def _get_data_from_path(driver_path: str, driver_data: dict) -> namedtuple:
    """
    Get driver information from driver filepath.
    """
    driver_data_format = namedtuple('driver_data_format', ['signed', 'path', 'name', 'description'])

    name = next((key for key, value in driver_data.items() if driver_path in value))
    description = driver_data[name][0]
    signed = driver_data[name][1]

    return driver_data_format(signed=signed, description=description, path=driver_path, name=name)
