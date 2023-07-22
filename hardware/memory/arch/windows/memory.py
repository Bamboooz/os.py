# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import wmi

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
    24: 'DDR4',
    25: 'LPDDR',
    26: 'LPDDR2',
    27: 'LPDDR3',
    28: 'LPDDR4',
    29: 'Logical non-volatile device',
    30: 'HBM',
    31: 'HBM2',
    32: 'DDR5',
    33: 'LPDDR5',
    34: 'DDR6',
    35: 'LPDDR6',
    36: 'DDR7',
    37: 'LPDDR7'
}


def capacity(per_stick=False) -> dict or int:
    capacities = {num: int(mem_module.Capacity) for num, mem_module in enumerate(wmi.WMI().Win32_PhysicalMemory())}

    m_capacity = sum(capacities.values())

    return capacities if per_stick else m_capacity


def sticks() -> int:
    capacities = capacity(per_stick=True)
    return len(capacities)


def factor(per_stick=False) -> dict or str:
    m_factors = {num: factors.get(mem_module.FormFactor) for num, mem_module in enumerate(wmi.WMI().Win32_PhysicalMemory())}

    return m_factors if per_stick else m_factors.get(0)


def m_type(per_stick=False) -> dict or str:
    m_types = {num: types.get(mem_module.MemoryType) for num, mem_module in enumerate(wmi.WMI().Win32_PhysicalMemory())}

    return m_types if per_stick else m_types.get(0)


def manufacturer(per_stick=False) -> dict or str:
    m_manufacturers = {num: mem_module.Manufacturer for num, mem_module in enumerate(wmi.WMI().Win32_PhysicalMemory())}

    return m_manufacturers if per_stick else m_manufacturers.get(0)


def clockspeed(per_stick=False) -> dict or int:
    m_clockspeeds = {num: int(mem_module.Speed) for num, mem_module in enumerate(wmi.WMI().Win32_PhysicalMemory())}

    return m_clockspeeds if per_stick else m_clockspeeds.get(0)


def serial(per_stick=False) -> dict or str:
    m_serials = {num: mem_module.SerialNumber for num, mem_module in enumerate(wmi.WMI().Win32_PhysicalMemory())}

    return m_serials if per_stick else m_serials.get(0)
