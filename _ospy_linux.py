# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os

POWER_SUPPLY_PATH = "/sys/class/power_supply"

BATTERIES = [battery for battery in os.listdir(POWER_SUPPLY_PATH) if battery.startswith('BAT') or 'battery' in battery.lower()]
HAS_BATTERY = False if not BATTERIES else True

BATTERY_STATUS_HIGH = 1
BATTERY_STATUS_LOW = 2
BATTERY_STATUS_CRITICAL = 4
BATTERY_STATUS_CHARGING = 8
BATTERY_STATUS_NO_BATTERY = 128
BATTERY_STATUS_FAILED = 255
