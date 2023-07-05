# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os


def get_drivers() -> dict:
    driver_locations = {}

    # Search for driver files in the specified directory
    driver_dirs = os.listdir('/sys/bus/')

    # Iterate over driver directories
    for driver_dir in driver_dirs:
        driver_path = f'/sys/bus/{driver_dir}/drivers/'

        # Check if the driver directory exists
        if os.path.exists(driver_path):
            drivers = os.listdir(driver_path)

            # Iterate over drivers within the directory
            for driver in drivers:
                driver_name = driver
                driver_location = os.path.join(driver_path, driver)
                driver_locations[driver_name] = driver_location

    return driver_locations
