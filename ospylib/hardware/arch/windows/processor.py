# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import winreg

from ospylib.common.registry import read_registry_value
from ospylib.common.prompt import execute_command

WMIC_CPU_MODEL = 'wmic cpu get name'
WMIC_CPU_CORES = 'wmic cpu get NumberOfLogicalProcessors'
WMIC_CPU_CLOCKSPEED = 'wmic cpu get maxclockspeed'
WMIC_CPU_ARCHITECTURE = 'wmic cpu get Architecture'
WMIC_CPU_VENDOR_ID = 'wmic cpu get manufacturer'

architectures = {
    0: "x86",
    5: "ARM",
    6: "Intel Itanium-based",
    9: "AMD64",
    10: "DEC Alpha",
    12: "ARM64",
    13: "MIPS",
    14: "MIPS64",
    15: "Power PC",
    16: "Power PC64",
    17: "SPARC",
    18: "SPARC64",
    20: "SHx",
    21: "SCx"
}

vendors = {
    "amdisbetter!": "AMD",
    "authenticamd": "AMD",
    "centaurhauls": "IDT WinChip/Centaur",
    "cyrixinstead": "Cyrix, STMicroelectronics, IBM",
    "genuineintel": "Intel",
    "transmetacpu": "Transmeta",
    "genuinetmx86": "Transmeta",
    "geodebynsc": "National Semiconductor",
    "nexgendriven": "NexGen",
    "riseriserise": "Rise",
    "sississis": "SiS",
    "umcumcumc": "UMC",
    "viaviavia": "VIA",
    "vortex86soc": "DM&P Vortex86",
    "shanghai": "Zhaoxin",
    "hygongenuine": "Hygon",
    "genuinerdc": "RDC Semiconductor Co. Ltd.",
    "e2kmachine": "MCST Elbrus",
}


class wmic:
    @staticmethod
    def model() -> str:
        model = execute_command(WMIC_CPU_MODEL, 1).strip()
        return model

    @staticmethod
    def cores() -> int:
        cores = execute_command(WMIC_CPU_CORES, 1).strip()
        return int(cores)

    @staticmethod
    def architecture() -> str:
        arch_value = int(execute_command(WMIC_CPU_ARCHITECTURE, 1).strip())
        architecture = architectures.get(arch_value, None)
        return architecture

    @staticmethod
    def clockspeed() -> int:
        clockspeed = execute_command(WMIC_CPU_CLOCKSPEED, 1).strip()
        return int(clockspeed)

    @staticmethod
    def vendor() -> str:
        vendor = execute_command(WMIC_CPU_VENDOR_ID, 1).strip()
        return vendor

    @staticmethod
    def manufacturer() -> str:
        vendor_id = execute_command(WMIC_CPU_VENDOR_ID, 1).strip()
        manufacturer = vendors.get(vendor_id.lower().replace(' ', ''), None)
        return manufacturer


class registry:
    @staticmethod
    def model() -> str:
        model = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "ProcessorNameString").strip()
        return model

    @staticmethod
    def cores() -> int:
        cpu_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor")
        num_cpus = winreg.QueryInfoKey(cpu_key)[0]
        winreg.CloseKey(cpu_key)
        return int(num_cpus)

    @staticmethod
    def architecture() -> str:
        architecture = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment", "PROCESSOR_ARCHITECTURE").strip()
        return architecture

    @staticmethod
    def clockspeed() -> int:
        clockspeed = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "~MHz")
        return clockspeed

    @staticmethod
    def vendor() -> str:
        vendor = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "VendorIdentifier").strip()
        return vendor

    @staticmethod
    def manufacturer() -> str:
        vendor_id = read_registry_value(winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\CentralProcessor\\0", "VendorIdentifier").strip()
        manufacturer = vendors.get(vendor_id.lower().replace(' ', ''), None)
        return manufacturer
