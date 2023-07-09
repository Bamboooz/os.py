# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os

from collections import namedtuple

from common.prompt.prompt import execute_command


def driver_query(driver: str=None) -> namedtuple or dict:
    """
    Returns a dict of drivers and information about them if driver not specified.
    {
        '<driver_name>': '<file_path>',
        ...
    }
    If driver name or driver path is specified, returns a named tuple with items:
        - name: Driver's name
        - path: Path to the driver file
        - description: Driver's description
    """
    if driver is not None and os.path.isfile(driver):
        return _get_data_from_path(driver)
    elif driver is not None:
        return _get_data_from_name(driver)

    kernel_release = execute_command('uname -r', 0)[0]
    driver_directory = f"/lib/modules/{kernel_release}/kernel/drivers/"
    driver_paths = [os.path.join(root, file) for root, dirs, files in os.walk(driver_directory) for file in files]
    drivers = [os.path.splitext(os.path.basename(file_path))[0] for file_path in driver_paths]

    driver_data = _get_driver_data(drivers, driver_paths)

    if driver is None and driver_data is not None:
        return {key: value for key, value in driver_data.items()}

    driver_data_format = namedtuple('driver_data_format', ['path', 'name', 'description'])
    driver_not_found = driver_data_format(path=None, name=None, description=None)
    return driver_not_found


def _get_driver_data(drivers: list, driver_paths: list) -> dict or None:
    """
    Put driver names and driver filepaths in a sorted dictionary.
    """
    try:
        driver_info = {
            driver_name: next((item for item in driver_paths if f'/{driver_name}.ko' in item), None)
            for driver_name in drivers
        }

        return {key: value for key, value in driver_info.items() if value is not None}  # Remove not found values
    except:
        return None


def _get_data_from_name(driver: str) -> namedtuple:
    """
    Get driver information from driver name.
    """
    driver_data_format = namedtuple('driver_data_format', ['path', 'name', 'description'])

    try:
        driver_data = execute_command(f'modinfo {driver}', 0)

        driver_path = None
        driver_description = None

        for line in driver_data:
            if line.startswith('filename:'):
                driver_path = line.replace('filename:', '').strip()
            elif line.startswith('description:'):
                driver_description = line.replace('description:', '').strip()

        if driver_path is not None and driver_description is not None:
            return driver_data_format(description=driver_description, path=driver_path, name=driver)
        else:
            raise Exception("Failed to get driver information.")
    except:
        return driver_data_format(description=None, path=None, name=None)


def _get_data_from_path(driver_path: str) -> namedtuple:
    """
    Get driver information from driver filepath.
    """
    driver_data_format = namedtuple('driver_data_format', ['path', 'name', 'description'])

    try:
        driver = os.path.splitext(os.path.basename(driver_path))[0]

        driver_data = execute_command(f'modinfo {driver}', 0)

        driver_description = None

        for line in driver_data:
            if line.startswith('description:'):
                driver_description = line.replace('description:', '').strip()

        if driver is not None and driver_description is not None:
            return driver_data_format(description=driver_description, path=driver_path, name=driver)
        else:
            raise Exception("Failed to get driver information.")
    except:
        return driver_data_format(description=None, path=None, name=None)
