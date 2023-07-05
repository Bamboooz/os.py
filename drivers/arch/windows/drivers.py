# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.prompt.prompt import execute_command


def get_drivers():
    driver_locations = {}

    output = execute_command("driverquery /fo csv /v /nh", trim=0, encodings=['cp1252'])

    # Process each line of the output
    for line in output:
        # Split the line by commas
        values = line.split(',')

        # Extract the driver name, description, signed status, and file path
        driver_name = values[0].strip('"')
        driver_description = values[1].strip('"')
        is_signed = values[7].strip('"').lower() == 'true'
        file_path = values[-2].strip('"')

        # Store the driver information in the dictionary
        driver_locations[driver_name] = [driver_description, is_signed, file_path]

    return driver_locations
