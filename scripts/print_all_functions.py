# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import re
import os
import sys


def extract_function_names(filename):  # extracting function names from a file
    with open(filename, 'r') as file:
        content = file.read()

    # Regular expression to match function names
    pattern = r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\("

    # Find all matches in the file
    matches = re.findall(pattern, content)

    return matches


def set_file_path_empty():  # clearing the file_path variable from the script
    with open(os.path.abspath(__file__), 'r') as f:
        lines = f.readlines()

    with open(os.path.abspath(__file__), 'w') as f:
        for line in lines:
            if line.replace(' ', '').startswith('file_path=r'):
                f.write("    file_path = r''\n")
            else:
                f.write(line)


if __name__ == '__main__':  # run the script
    file_path = r''

    if os.path.exists(file_path):
        for function in extract_function_names(file_path):
            print(f'print({function}())')

        set_file_path_empty()
    else:
        print('Error: file not found.')
        sys.exit(-1)
