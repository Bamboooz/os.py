# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import subprocess

def execute_command(command, trim):
    result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.DEVNULL)
    lines = result.split('\n')

    if 0 < trim <= len(lines):
        lines = lines[trim:]

    lines = [line for line in lines if line.strip()]  # Remove empty lines

    output = '\n'.join(lines)
    return output
