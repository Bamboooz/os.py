import multiprocessing
import platform

import os_py.arch.win32._winutil as _winutils

from scripts import _common


class WINREG_KEYS:
    WIN32_CPU_MODEL_KEY = [r"Hardware\Description\System\CentralProcessor\0", "ProcessorNameString"]
    WIN32_CPU_CLOCKSPEED_KEY = [r"Hardware\Description\System\CentralProcessor\0", "~Mhz"]
    WIN32_CPU_VENDOR_ID = [r"Hardware\Description\System\CentralProcessor\0", "VendorIdentifier"]


class WMI_CMD:
    WMI_CPU_MODEL = 'wmic cpu get name'
    WMI_CPU_CLOCKSPEED = 'wmic cpu get maxclockspeed'
    WMI_CPU_VENDOR_ID = 'wmic cpu get manufacturer'


def win32_get_cpu_model(method='wmic'):
    def win32_model_wmic():
        return _winutils.run_and_get_stdout(WMI_CMD.WMI_CPU_MODEL)

    def win32_model_winreg():
        processor_brand = _winutils.read_windows_registry_key(WINREG_KEYS.WIN32_CPU_MODEL_KEY)
        return processor_brand.strip()

    if method.lower() == 'wmic':
        return win32_model_wmic()
    elif method.lower() == 'winreg':
        return win32_model_winreg()


def win32_get_cpu_total_cores():
    return multiprocessing.cpu_count()


def win32_get_cpu_clockspeed(method='wmic'):
    def win32_clockspeed_wmic():
        return _winutils.run_and_get_stdout(WMI_CMD.WMI_CPU_CLOCKSPEED) + 'MHz'

    def win32_clockspeed_winreg():
        hz_actual = _winutils.read_windows_registry_key(WINREG_KEYS.WIN32_CPU_CLOCKSPEED_KEY)
        hz_actual = _common.Unit().hz_short_to_friendly(hz_actual, 6)
        return hz_actual

    if method.lower() == 'wmic':
        return win32_clockspeed_wmic()
    elif method.lower() == 'winreg':
        return win32_clockspeed_winreg()


def win32_get_cpu_architecture():
    return platform.machine()


def win32_get_cpu_bits():
    return platform.architecture()[0]


def win32_get_cpu_manufacturer(method='wmic'):
    return {
        "amdisbetter!": "AMD",
        "authenticamd": "AMD",
        "centaurhauls": "IDT WinChip/Centaur",
        "cyrixinstead": "Cyrix, STMicroelectronics, IBM",
        "genuineintel": "Intel",
        "transmetacpu": "Transmeta",
        "genuinetmx86": "Transmeta",
        "geode by nsc": "National Semiconductor",
        "nexgendriven": "NexGen",
        "riseriserise": "Rise",
        "sis sis sis ": "SiS",
        "umc umc umc ": "UMC",
        "via via via ": "VIA",
        "vortex86 soc": "DM&P Vortex86",
        "  shanghai  ": "Zhaoxin",
        "hygongenuine": "Hygon",
        "genuine  rdc": "RDC Semiconductor Co. Ltd.",
        "e2k machine": "MCST Elbrus",
        "not detected": "Not detected"
    }[win32_get_cpu_vendor_id(method).lower()]


def win32_get_cpu_vendor_id(method='wmic'):
    def win32_vendor_id_wmic():
        return _winutils.run_and_get_stdout(WMI_CMD.WMI_CPU_VENDOR_ID)

    def win32_vendor_id_winreg():
        vendor_id_raw = _winutils.read_windows_registry_key(WINREG_KEYS.WIN32_CPU_VENDOR_ID)
        return vendor_id_raw

    if method.lower() == 'wmic':
        return win32_vendor_id_wmic()
    elif method.lower() == 'winreg':
        return win32_vendor_id_winreg()
    else:
        return 'Not detected'
