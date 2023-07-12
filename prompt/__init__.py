# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import argparse
import system

RED = '\033[91m'
GREEN = '\033[92m'
DARK_CYAN = '\033[36m'
END_COLOR = '\033[0m'


def from_cmd():
    print(DARK_CYAN + '> ospylib system and hardware information library report' + END_COLOR)
    print(GREEN     + '> Gathering system information, progress: 59%' + END_COLOR)  # random number for now this file won't even work until the c code will work with python 💀
    return

def from_filepath(filepath):
    # Function implementation for filepath
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Specify a file path you want to store ospylib information in.')
    args = parser.parse_args()

    if system.name() == 'Windows':
        os.system('color')

    if args.file:
        if args.file:
            from_filepath(args.file)
        else:
            print(RED + 'Error: File path not provided.' + END_COLOR)
            exit(-1)
    else:
        from_cmd()


if __name__ == '__main__':
    main()
