# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys as system
from ospy import sys


if __name__ == '__main__':
    # simple_example.py - runs the program if the user is running Windows, raise an error otherwise.

    if sys.get_os_info()['name'].lower() == 'windows':
        print('Application executed successfully!')
    else:
        print('Error: Unsupported operating system.')
        system.exit(-1)
