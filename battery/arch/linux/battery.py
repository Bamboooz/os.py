# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from collections import namedtuple

from _ospy_linux import *


def sensors_battery() -> namedtuple:
    bat_stat = namedtuple('bat_stat', ['percent', 'time_left', 'charging', 'flag', 'present'])

    if HAS_BATTERY is False:
        battery = bat_stat(percent=None, time_left=None, charging=None, flag=None, present=False)
        return battery




# Access the fields of the named tuple
print(sensors_battery().percent)
print(sensors_battery().time_left)
print(sensors_battery().charging)
print(sensors_battery().flag)
print(sensors_battery().present)