# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
These are my notes which present ospylib functionality when I will finally finish it.
"""

# -------------------- #
# ospylib audio module #
# -------------------- #

_ = ospylib.audio_devices().input
_ = ospylib.audio_devices().output

# --------------------- #
# ospylib device module #
# --------------------- #

_ = ospylib.ext_dev().removables

"""
{
    '<letter>': ['<name>', '<fstype>']
}
"""

_ = ospylib.ext_dev().total

# like 1

# ---------------------- #
# ospylib display module #
# ---------------------- #

x, y = ospylib.display().resolution
_ = ospylib.display().refreq

# ---------------------- #
# ospylib drivers module #
# ---------------------- #

_ = ospylib.drivers()

"""
example return:
{
    '<name>': ['<description>', <signed>, '<path>'],
    ...
}
"""

_ = ospylib.drivers(name or path).description
_ = ospylib.drivers(name or path).signed
_ = ospylib.drivers(name or path).location

# ----------------------- #
# ospylib hardware module #
# ----------------------- #

_ = ospylib.cpu_count(logical=True, physical=True)  # which of those include in the returned int so if both false returns 0
_ = ospylib.cpu().model
_ = ospylib.cpu().vendor
_ = ospylib.cpu().manufacturer
_ = ospylib.cpu().type
_ = ospylib.cpu().clockspeed
_ = ospylib.cpu_supports(feature=CPU_FEATURE_SSSE3)  # there will be many more features

_ = ospylib.gpu().model
_ = ospylib.gpu().total
_ = ospylib.gpu().used
_ = ospylib.gpu().free
_ = ospylib.gpu().serial

_ = ospylib.baseboard().product
_ = ospylib.baseboard().serial
_ = ospylib.baseboard().version

_ = ospylib.memory().capacity
_ = ospylib.memory().sticks
_ = ospylib.memory().factor
_ = ospylib.memory().type
_ = ospylib.memory().manufacturer
_ = ospylib.memory().clockspeed
_ = ospylib.memory().serial

_ = ospylib.swap().total
_ = ospylib.swap().used
_ = ospylib.swap().free

# ---------------------- #
# ospylib sensors module #
# ---------------------- #

_ = ospylib.sensors_usage().cpu
_ = ospylib.sensors_usage().gpu
_ = ospylib.sensors_usage().ram
_ = ospylib.sensors_usage().swap

_ = ospylib.sensors_temperature().cpu
_ = ospylib.sensors_temperature().gpu

_ = ospylib.sensors_fans().cpu
_ = ospylib.sensors_fans().gpu

_ = ospylib.sensors_volatge().cpu
_ = ospylib.sensors_volatge().gpu

_ = ospylib.sensors_power().cpu # i guess like power usage in kWh?
_ = ospylib.sensors_power().gpu

_ = ospylib.sensors_battery().percentage
_ = ospylib.sensors_battery().present
_ = ospylib.sensors_battery().flag
_ = ospylib.sensors_battery().time_left
_ = ospylib.sensors_battery().charging

# -------------------------- #
# ospylib peripherals module #
# -------------------------- #

_ = ospylib.mouse().model
_ = ospylib.mouse().dpi
_ = ospylib.mouse().driver

_ = ospylib.keyboard().model
_ = ospylib.keyboard().layout
_ = ospylib.keyboard().lang
_ = ospylib.keyboard().driver

_ = ospylib.webcam().model
_ = ospylib.webcam().resolution
_ = ospylib.webcam().driver

# ---------------------- #
# ospylib storage module #
# ---------------------- #

_ = ospylib.disk_usage(drive='C://').total
_ = ospylib.disk_usage(drive='C://').used
_ = ospylib.disk_usage(drive='C://').free
_ = ospylib.disk_usage(drive='C://').perc_free
_ = ospylib.disk_usage(drive='C://').perc_used

_ = ospylib.disk_partitions(drive='C://').fstype
_ = ospylib.disk_partitions(drive='C://').type.removable
_ = ospylib.disk_partitions(drive='C://').type.mount
_ = ospylib.disk_partitions(drive='C://').type.drive

# --------------------- #
# ospylib system module #
# --------------------- #

name = ospylib.system().name
hostname = ospylib.system().hostname
version = ospylib.system().version
platform = ospylib.system().platform
release = ospylib.system().release
arch = ospylib.system().architecture
user, is_admin = ospylib.system().user
lang, encoding = ospylib.system().lang
uptime = ospylib.system().uptime

# windows only
is_safe_mode = ospylib.system().safe_mode
has_hvci = ospylib.system().hvci

# and im not yet sure what will i put in process