# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os


LICENSE_INFO_PYTHON = '''# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

'''

LICENSE_INFO_CPP = '''/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

'''


def add_license_header(file_path):
    _, ext = os.path.splitext(file_path)
    if ext == '.py':
        header = LICENSE_INFO_PYTHON
    elif ext in ['.c', '.h']:
        header = LICENSE_INFO_CPP
    else:
        return

    with open(file_path, 'r+', encoding='utf-8') as f:
        content = f.read()
        if not content.startswith(header):
            f.seek(0)
            f.write(header + content)
            print(f'Successfully added copyright notice to: {file_path}')


if __name__ == "__main__":
    DIR = r""  # the os.py code directory if you got this scripts in the script folder

    for root, dirs, files in os.walk(DIR):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            add_license_header(file_path)
