# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os


LICENSE_INFO = '''# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

'''


DIRECTORY = '\\'.join(os.getcwd().split('\\')[:-1])  # default working directory if you keep the scripts in the os.py/scripts directory


def add_license(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r+') as f:
                    content = f.read()
                    if content.startswith(LICENSE_INFO):
                        continue
                    f.seek(0, 0)
                    f.write(LICENSE_INFO + content)


if __name__ == '__main__':
    add_license(DIRECTORY)
