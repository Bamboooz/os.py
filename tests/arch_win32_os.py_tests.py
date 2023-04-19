# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import datetime

from ospy import *


print(f"[os.py information dump file, dump created on {datetime.datetime.now()}]:\n")

for key, value in sys.get_os_info().items():
    print(f"os {key}: {value}")

for key, value in cpu.get_processor_info().items():
    print(f"cpu {key}: {value}")

for key, value in gpu.get_graphics_card_info().items():
    print(f"gpu {key}: {value}")

for key, value in memory.get_ram_info().items():
    print(f"ram {key}: {value}")

print(f'available drives {storage.get_drive_list()}')

for key, value in storage.get_drive_info().items():
    print(f"storage {key}: {value}")

for key, value in motherboard.get_motherboard_info().items():
    print(f"motherboard {key}: {value}")

print(f'number of connected external devices: {device.get_number_of_external_drives()}')
print(f'external drives: {device.get_external_drives()}')
print(f'firmware type: {machine.get_firmware_type()}')
