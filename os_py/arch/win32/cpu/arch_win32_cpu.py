import os_py.arch.win32.cpu._libcpu as libcpu
import os_py.arch.win32._winutil as _winutil


def win32_get_cpu_model():
    if _winutil.DataSources().wmic_available(libcpu.WMI_CMD.WMI_CPU_MODEL):
        return libcpu.win32_get_cpu_model('wmic')
    elif _winutil.DataSources().regedit_available(libcpu.WINREG_KEYS.WIN32_CPU_MODEL_KEY):
        return libcpu.win32_get_cpu_model('winreg')
    else:
        return 'Not detected'


def win32_get_cpu_total_cores():
    return libcpu.win32_get_cpu_total_cores()


def win32_get_cpu_clockspeed():
    if _winutil.DataSources().wmic_available(libcpu.WMI_CMD.WMI_CPU_CLOCKSPEED):
        return libcpu.win32_get_cpu_clockspeed('wmic')
    elif _winutil.DataSources().regedit_available(libcpu.WINREG_KEYS.WIN32_CPU_CLOCKSPEED_KEY):
        return libcpu.win32_get_cpu_clockspeed('winreg')
    else:
        return 'Not detected'


def win32_get_cpu_architecture():
    return libcpu.win32_get_cpu_architecture()


def win32_get_cpu_bits():
    return libcpu.win32_get_cpu_bits()


def win32_get_cpu_manufacturer():
    if _winutil.DataSources().wmic_available(libcpu.WMI_CMD.WMI_CPU_VENDOR_ID):
        return libcpu.win32_get_cpu_manufacturer('wmic')
    elif _winutil.DataSources().regedit_available(libcpu.WINREG_KEYS.WIN32_CPU_VENDOR_ID):
        return libcpu.win32_get_cpu_manufacturer('winreg')
    else:
        return 'Not detected'


def win32_get_cpu_vendor_id():
    if _winutil.DataSources().wmic_available(libcpu.WMI_CMD.WMI_CPU_VENDOR_ID):
        return libcpu.win32_get_cpu_vendor_id('wmic')
    elif _winutil.DataSources().regedit_available(libcpu.WINREG_KEYS.WIN32_CPU_VENDOR_ID):
        return libcpu.win32_get_cpu_vendor_id('winreg')
    else:
        return 'Not detected'
