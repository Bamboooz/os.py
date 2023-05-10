# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import multiprocessing
import platform
import winreg

from ospy import toolbox

# Windows registry keys for retrieving CPU information
WINREG_CPU_MODEL = [winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0", "ProcessorNameString"]
WINREG_CPU_CLOCKSPEED = [winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0", "~Mhz"]
WINREG_CPU_ARCHITECTURE = [winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment", 'PROCESSOR_ARCHITECTURE']
WINREG_CPU_VENDOR_ID = [winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0", "VendorIdentifier"]

# WMIC commands for retrieving CPU information
WMIC_CPU_MODEL = 'wmic cpu get name'
WMIC_CPU_CLOCKSPEED = 'wmic cpu get maxclockspeed'
WMIC_CPU_ARCHITECTURE = 'wmic cpu get Architecture'
WMIC_CPU_VENDOR_ID = 'wmic cpu get manufacturer'

# Define a dictionary to map Architecture value to CPU architecture name
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

# Define a dictionary to map CPU vendor id codes to the actual product manufacturers
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


def multiprocessing_get_cpu_total_cores():
    """Get the total number of CPU cores using the multiprocessing module"""
    return multiprocessing.cpu_count()


def platform_get_cpu_architecture():
    """Get the CPU architecture using the platform module"""
    return platform.machine()


def wmic_get_cpu_model():
    """Get the CPU model using the Windows Management Instrumentation Command-line (WMIC)"""
    return toolbox.parse_wmic(WMIC_CPU_MODEL)[1]['output']


def wmic_get_cpu_clockspeed():
    """Get the CPU clock speed using WMIC"""
    return toolbox.parse_wmic(WMIC_CPU_CLOCKSPEED)[1]['output']


def wmic_get_cpu_architecture():
    """Get the CPU architecture using WMIC"""
    arch_value = int(toolbox.parse_wmic(WMIC_CPU_ARCHITECTURE)[1]['output'])
    architecture = architectures.get(arch_value, None)

    # Raise an exception if architecture is not recognized
    if architecture is None: raise Exception()

    return architecture

def wmic_get_cpu_vendor_id():
    """Get the CPU vendor ID using WMIC"""
    return toolbox.parse_wmic(WMIC_CPU_VENDOR_ID)[1]['output']


def wmic_get_cpu_manufacturer():
    """Get the CPU manufacturer name using WMIC"""
    vendor_id = toolbox.parse_wmic(WMIC_CPU_VENDOR_ID)[1]['output']
    manufacturer = vendors.get(vendor_id.lower().replace(' ', ''), None)

    # Raise an exception if architecture is not recognized
    if manufacturer is None: raise Exception()

    return manufacturer


def winreg_get_cpu_model():
    """Get the CPU model using the Windows registry"""
    return toolbox.load_winreg_key(WINREG_CPU_MODEL)


def winreg_get_cpu_clockspeed():
    """Get the CPU clock speed using the Windows registry"""
    return toolbox.load_winreg_key(WINREG_CPU_CLOCKSPEED)


def winreg_get_cpu_architecture():
    """Get CPU architecture using Windows Registry"""
    return toolbox.load_winreg_key(WINREG_CPU_ARCHITECTURE)


def winreg_get_cpu_vendor_id():
    """Get CPU vendor ID using Windows Registry"""
    return toolbox.load_winreg_key(WINREG_CPU_VENDOR_ID)


def winreg_get_cpu_manufacturer():
    """Get CPU manufacturer using Windows Registry"""
    vendor_id = toolbox.load_winreg_key(WINREG_CPU_VENDOR_ID)
    manufacturer = vendors.get(vendor_id.lower().replace(' ', ''), None)

    # Raise an exception if architecture is not recognized
    if manufacturer is None: raise Exception()

    return manufacturer
