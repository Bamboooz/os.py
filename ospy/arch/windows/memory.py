# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from ospy.arch.windows import wintools


# Define GB as a constant
GB = 1024 * 1024 * 1024

# Define WMIC commands to get RAM information
WMIC_CAPACITY = "wmic memorychip get capacity"
WMIC_FORM_FACTOR = "wmic memorychip get formfactor"
WMIC_MANUFACTURER = "wmic memorychip get manufacturer"
WMIC_MEMORY_TYPE = "wmic memorychip get memorytype"
WMIC_MODEL = "wmic memorychip get model"
WMIC_CLOCKSPEED = "wmic memorychip get speed"
WMIC_SERIAL_NUMBER = "wmic memorychip get serialnumber"

# Define WMIC keys to retrieve RAM form factor
factors = {
    0: None,
    1: 'Other',
    2: 'SIP',
    3: 'DIP',
    4: 'ZIP',
    5: 'SOJ',
    6: 'Proprietary',
    7: 'SIMM',
    8: 'DIMM',
    9: 'TSOP',
    10: 'PGA',
    11: 'RIMM',
    12: 'SODIMM',
    13: 'SRIMM',
    14: 'SMD',
    15: 'SSMP',
    16: 'QFP',
    17: 'TQFP',
    18: 'SOIC',
    19: 'LCC',
    20: 'PLCC',
    21: 'BGA',
    22: 'FPBGA',
    23: 'LGA',
    24: 'FB-DIMM'
}

# Define WMIC keys for RAM types
types = {
    0: None,
    1: 'Other',
    2: 'DRAM',
    3: 'Synchronous DRAM',
    4: 'Cache DRAM',
    5: 'EDO',
    6: 'EDRAM',
    7: 'VRAM',
    8: 'SRAM',
    9: 'RAM',
    10: 'ROM',
    11: 'Flash',
    12: 'EEPROM',
    13: 'FEPROM',
    14: 'EPROM',
    15: 'CDRAM',
    16: '3DRAM',
    17: 'SDRAM',
    18: 'SGRAM',
    19: 'RDRAM',
    20: 'DDR',
    21: 'DDR2',
    22: 'DDR2 FB-DIMM',
    23: 'DDR3',
    24: 'FBD2',
    25: 'DDR4'
}


def wmic_get_ram_capacity():
    """Uses WMIC to retrieve the RAM capacity."""
    capacities = {}

    for stick in wintools.parse_wmic(WMIC_CAPACITY):
        capacities[stick] = round(float(wintools.parse_wmic(WMIC_CAPACITY)[stick]['output']), 2) / GB

    return capacities


wmic_get_ram_capacity()
def wmic_get_ram_sticks_number():
    """Uses WMIC to retrieve the number of RAM sticks."""
    return len(wintools.parse_wmic(WMIC_CAPACITY))


def wmic_get_ram_form_factor():
    """Uses WMIC to retrieve the RAM form factor."""
    form_factors = {}

    for stick in wintools.parse_wmic(WMIC_FORM_FACTOR):
        form_factors[stick] = factors.get(int(wintools.parse_wmic(WMIC_FORM_FACTOR)[1]['output']), None)

    return form_factors


def wmic_get_ram_memory_type():
    """Uses WMIC to retrieve the RAM memory type."""
    mem_types = {}

    for stick in wintools.parse_wmic(WMIC_FORM_FACTOR):
        mem_types[stick] = factors.get(int(wintools.parse_wmic(WMIC_MEMORY_TYPE)[1]['output']), None)

    return mem_types


def wmic_get_ram_manufacturer():
    """Uses WMIC to retrieve the RAM manufacturer."""
    manufacturers = {}

    for stick in wintools.parse_wmic(WMIC_MANUFACTURER):
        manufacturers[stick] = wintools.parse_wmic(WMIC_MANUFACTURER)[stick]['output']

    return manufacturers


def wmic_get_ram_clockspeed():
    """Uses WMIC to retrieve the RAM clockspeed."""
    clock_speeds = {}

    for stick in wintools.parse_wmic(WMIC_CLOCKSPEED):
        clock_speeds[stick] = wintools.parse_wmic(WMIC_CLOCKSPEED)[stick]['output']

    return clock_speeds


def wmic_get_ram_serial_number():
    """Uses WMIC to retrieve the RAM serial number."""
    serial_numbers = {}

    for stick in wintools.parse_wmic(WMIC_SERIAL_NUMBER):
        serial_numbers[stick] = wintools.parse_wmic(WMIC_SERIAL_NUMBER)[stick]['output']

    return serial_numbers
