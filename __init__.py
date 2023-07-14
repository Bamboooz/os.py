# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from system import *
from storage import *
from drivers import *
from display import *
from device import *
from audio import *
from peripherals import *
from firmware import *
from process import *

from hardware.baseboard import *
from hardware.graphics import *
from hardware.memory import *
from hardware.processor import *
from hardware.swap import *

from sensors.battery import *
from sensors.fans import *
from sensors.usage import *
from sensors.voltage import *
from sensors.temperature import *


__author__ = "Bamboooz"
__repo__ = "https://github.com/Bamboooz/os.py"
__version__ = "0.0.1"
__supported_os__ = ['Windows', 'Linux']
__os__ = name()


if __os__ not in __supported_os__:
    raise OSError(f"Unsupported by ospylib operating system: {__os__}.")
