# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


def layout():
    with open('/etc/default/keyboard', 'r') as file:
        lines = file.read().splitlines()

    for line in lines:
        if line.startswith('XKBLAYOUT'):
            layout = line.split('=')[1].replace('"', '')
            return layout

    return None
