# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from ospylib.common.prompt import execute_command

WMIC_CAPACITY = "wmic memorychip get capacity"
WMIC_FORM_FACTOR = "wmic memorychip get formfactor"
WMIC_MANUFACTURER = "wmic memorychip get manufacturer"
WMIC_MEMORY_TYPE = "wmic memorychip get memorytype"
WMIC_CLOCKSPEED = "wmic memorychip get speed"
WMIC_SERIAL_NUMBER = "wmic memorychip get serialnumber"

POWERSHELL_CAPACITY = "powershell.exe -Command \"Get-WmiObject -Class Win32_PhysicalMemory | Select-Object -ExpandProperty Capacity\""
POWERSHELL_FORM_FACTOR = "powershell.exe -Command \"Get-WmiObject -Class Win32_PhysicalMemory | Select-Object -ExpandProperty FormFactor\""
POWERSHELL_MANUFACTURER = "powershell.exe -Command \"Get-WmiObject -Class Win32_PhysicalMemory | Select-Object -ExpandProperty Manufacturer\""
POWERSHELL_MEMORY_TYPE = "powershell.exe -Command \"Get-WmiObject -Class Win32_PhysicalMemory | Select-Object -ExpandProperty Memorytype\""
POWERSHELL_CLOCKSPEED = "powershell.exe -Command \"Get-WmiObject -Class Win32_PhysicalMemory | Select-Object -ExpandProperty Speed\""
POWERSHELL_SERIAL_NUMBER = "powershell.exe -Command \"Get-WmiObject -Class Win32_PhysicalMemory | Select-Object -ExpandProperty Serialnumber\""

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


class wmic:
    @staticmethod
    def capacity() -> dict:
        capacities = {}

        for stick, value in enumerate(execute_command(WMIC_CAPACITY, 1).split('\n')):
            capacities[stick] = float(value.strip())

        return capacities

    def sticks(self) -> int:
        return len(self.capacity())

    @staticmethod
    def factor() -> dict:
        form_factors = {}

        for stick, value in enumerate(execute_command(WMIC_FORM_FACTOR, 1).split('\n')):
            form_factors[stick] = factors.get(int(value.strip()), None)

        return form_factors

    @staticmethod
    def m_type() -> dict:
        mem_types = {}

        for stick, value in enumerate(execute_command(WMIC_MEMORY_TYPE, 1).split('\n')):
            mem_types[stick] = types.get(int(value.strip()), None)

        return mem_types

    @staticmethod
    def manufacturer() -> dict:
        manufacturers = {}

        for stick, value in enumerate(execute_command(WMIC_MANUFACTURER, 1).split('\n')):
            manufacturers[stick] = value.strip()

        return manufacturers

    @staticmethod
    def clockspeed() -> dict:
        clock_speeds = {}

        for stick, value in enumerate(execute_command(WMIC_CLOCKSPEED, 1).split('\n')):
            clock_speeds[stick] = value.strip()

        return clock_speeds

    @staticmethod
    def serial() -> dict:
        serial_numbers = {}

        for stick, value in enumerate(execute_command(WMIC_SERIAL_NUMBER, 1).split('\n')):
            serial_numbers[stick] = value.strip()

        return serial_numbers


class powershell:
    @staticmethod
    def capacity() -> dict:
        capacities = {}

        for stick, value in enumerate(execute_command(POWERSHELL_CAPACITY, 0).split('\n')):
            capacities[stick] = float(value.strip())

        return capacities

    def sticks(self) -> int:
        return len(self.capacity())

    @staticmethod
    def factor() -> dict:
        form_factors = {}

        for stick, value in enumerate(execute_command(POWERSHELL_FORM_FACTOR, 0).split('\n')):
            form_factors[stick] = factors.get(int(value.strip()), None)

        return form_factors

    @staticmethod
    def m_type() -> dict:
        mem_types = {}

        for stick, value in enumerate(execute_command(POWERSHELL_MEMORY_TYPE, 0).split('\n')):
            mem_types[stick] = types.get(int(value.strip()), None)

        return mem_types

    @staticmethod
    def manufacturer() -> dict:
        manufacturers = {}

        for stick, value in enumerate(execute_command(POWERSHELL_MANUFACTURER, 0).split('\n')):
            manufacturers[stick] = value.strip()

        return manufacturers

    @staticmethod
    def clockspeed() -> dict:
        clock_speeds = {}

        for stick, value in enumerate(execute_command(POWERSHELL_CLOCKSPEED, 0).split('\n')):
            clock_speeds[stick] = value.strip()

        return clock_speeds

    @staticmethod
    def serial() -> dict:
        serial_numbers = {}

        for stick, value in enumerate(execute_command(POWERSHELL_SERIAL_NUMBER, 0).split('\n')):
            serial_numbers[stick] = value.strip()

        return serial_numbers
