# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import winreg

from common.regedit.registry import read_registry_value
from common.prompt.prompt import execute_command
from common.cpuid.types import *


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

    def manufacturer(self) -> str:
        vendor_id = self.vendor()
        manufacturer = vendor_map.get(vendor_id, [None, None])[0]
        return manufacturer

    def cpu_type(self) -> str:
        vendor_id = self.vendor()
        cpu_type = vendor_map.get(vendor_id, [None, None])[1]
        return cpu_type


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

    def manufacturer(self) -> str:
        vendor_id = self.vendor()
        manufacturer = vendor_map.get(vendor_id, [None, None])[0]
        return manufacturer

    def cpu_type(self) -> str:
        vendor_id = self.vendor()
        cpu_type = vendor_map.get(vendor_id, [None, None])[1]
        return cpu_type
