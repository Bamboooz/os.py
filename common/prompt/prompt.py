# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import subprocess


def execute_command(command, trim, encodings=None):  # refactor to check for the correct encoding system itself, remove shell=True as it poses security issues
    if encodings is None:
        encodings = ['utf-8']

    output = None
    for encoding in encodings:
        try:
            result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.DEVNULL,
                                             encoding=encoding)
            output = result.strip()
            break
        except UnicodeDecodeError:
            continue

    if output is None:
        raise ValueError("Failed to decode command output using available encodings.")

    lines = output.split('\n')

    if 0 < trim <= len(lines):
        lines = lines[trim:]

    lines = [line for line in lines if line.strip()]  # Remove empty lines

    return lines
