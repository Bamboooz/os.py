# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import argparse
import sys as system

from os_py import *


def print_output_to_command_prompt():
    print(f"[os.py information dump file, dump created on {datetime.datetime.now()}]:\n")

    for key, value in sys.get_os_info().items():
        print(f"os {key}: {value}")

    for key, value in cpu.get_processor_info().items():
        print(f"cpu {key}: {value}")

    for key, value in gpu.get_graphics_card_info().items():
        print(f"gpu {key}: {value}")

    for key, value in memory.get_ram_info().items():
        print(f"ram {key}: {value}")

    print(f'available drives {storage.get_drive_list()}')

    for key, value in storage.get_drive_info().items():
        print(f"storage {key}: {value}")

    for key, value in motherboard.get_motherboard_info().items():
        print(f"motherboard {key}: {value}")

    print(f'number of connected external devices: {device.get_number_of_external_drives()}')
    print(f'external drives: {device.get_external_drives()}')
    print(f'firmware type: {machine.get_firmware_type()}')

def dump_os_py_data_to_txt_file(chosen_file):
    with open(chosen_file, 'w') as f:
        f.write(f"[os.py information dump file, dump created on {datetime.datetime.now()}]:\n")

        for key, value in sys.get_os_info().items():
            f.write(f"os {key}: {value}")

        for key, value in cpu.get_processor_info().items():
            f.write(f"cpu {key}: {value}")

        for key, value in gpu.get_graphics_card_info().items():
            f.write(f"gpu {key}: {value}")

        for key, value in memory.get_ram_info().items():
            f.write(f"ram {key}: {value}")

        f.write(f'available drives {storage.get_drive_list()}')

        for key, value in storage.get_drive_info().items():
            f.write(f"storage {key}: {value}")

        for key, value in motherboard.get_motherboard_info().items():
            f.write(f"motherboard {key}: {value}")

        f.write(f'number of connected external devices: {device.get_number_of_external_drives()}')
        f.write(f'external drives: {device.get_external_drives()}')
        f.write(f'firmware type: {machine.get_firmware_type()}')


if __name__ == '__main__':
    # Create the parser object
    parser = argparse.ArgumentParser(description='os.py command line tool to gather system and hardware information.')

    # Add the arguments
    parser.add_argument('--dump', default=None, choices=['cmd', 'txt'], help='Specify dump type (default: cmd)')
    parser.add_argument('--file', default=None, help='Specify file name')

    # Parse the arguments
    args = parser.parse_args()

    # Check if both arguments are specified
    if args.file and args.dump == 'cmd':
        print('Error: cmd argument cannot be run with the file argument')
        system.exit(-1)

    if args.dump is None: args.dump = 'cmd'

    # Check if both arguments are specified
    if args.file is None and args.dump == 'txt':
        print('Error: file argument must be specified when using txt dump method', file=system.stderr)
        system.exit(-1)

    # Set the dump value to 'txt' if file is specified
    if args.file:
        args.dump = 'txt'

    # check if specified file exists
    if args.dump == 'txt':
        try:
            with open(args.file, 'r') as file:
                pass
        except:
            print('Error: file not found.')
            system.exit(-1)

    if args.dump == 'cmd':
        print_output_to_command_prompt()
    else:
        dump_os_py_data_to_txt_file(args.file)
