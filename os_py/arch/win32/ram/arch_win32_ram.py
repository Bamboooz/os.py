import os_py.arch.win32.ram._libram as libram
import os_py.arch.win32._winutil as _winutil


def win32_ram_capacity():
    if _winutil.DataSources().wmic_available(libram.WMI_MEMORYCHIP.WIN32_WMI_CAPACITY):
        return libram.win32_ram_capacity('wmic')
    else:
        return 'Not detected'


def win32_ram_form_factor():
    if _winutil.DataSources().wmic_available(libram.WMI_MEMORYCHIP.WIN32_WMI_FORM_FACTOR):
        return libram.win32_ram_form_factor('wmic')
    else:
        return 'Not detected'


def win32_ram_memory_type():
    if _winutil.DataSources().wmic_available(libram.WMI_MEMORYCHIP.WIN32_WMI_MEMORY_TYPE):
        return libram.win32_ram_memory_type('wmic')
    else:
        return 'Not detected'


def win32_ram_manufacturer():
    if _winutil.DataSources().wmic_available(libram.WMI_MEMORYCHIP.WIN32_WMI_MANUFACTURER):
        return libram.win32_ram_manufacturer('wmic')
    else:
        return 'Not detected'


def win32_ram_clockspeed():
    if _winutil.DataSources().wmic_available(libram.WMI_MEMORYCHIP.WIN32_WMI_CLOCKSPEED):
        return libram.win32_ram_clockspeed('wmic')
    else:
        return 'Not detected'


def win32_ram_serial_number():
    if _winutil.DataSources().wmic_available(libram.WMI_MEMORYCHIP.WIN32_WMI_SERIAL_NUMBER):
        return libram.win32_ram_serial_number('wmic')
    else:
        return 'Not detected'
