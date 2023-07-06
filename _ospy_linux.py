# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os

POWER_SUPPLY_PATH = "/sys/class/power_supply"

_batteries = [battery for battery in os.listdir(POWER_SUPPLY_PATH) if battery.startswith('BAT') or 'battery' in battery.lower()]
HAS_BATTERY = False if _batteries is None else True
