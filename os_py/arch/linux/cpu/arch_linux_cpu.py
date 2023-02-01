import os_py.arch.linux.cpu._libcpu as libcpu
import os_py.arch.linux._linuxutil as _linuxutil


def win32_get_cpu_model():
    if _linuxutil.is_lscpu_available():
        return libcpu.linux_get_cpu_model('lscpu')
    elif _linuxutil.is_procinfo_available():
        return libcpu.linux_get_cpu_model('proc')
    else:
        return 'Not detected'


def win32_get_cpu_total_cores():
    return libcpu.linux_get_cpu_total_cores()


def win32_get_cpu_clockspeed():
    if _linuxutil.is_procinfo_available():
        return libcpu.linux_get_cpu_clockspeed('proc')
    else:
        return 'Not detected'


def win32_get_cpu_architecture():
    return libcpu.linux_get_cpu_architecture()


def win32_get_cpu_bits():
    return libcpu.linux_get_cpu_bits()


def win32_get_cpu_manufacturer():
    if _linuxutil.is_lscpu_available():
        return libcpu.linux_get_cpu_manufacturer('lscpu')
    elif _linuxutil.is_procinfo_available():
        return libcpu.linux_get_cpu_manufacturer('proc')
    else:
        return 'Not detected'


def win32_get_cpu_vendor_id():
    if _linuxutil.is_lscpu_available():
        return libcpu.linux_get_cpu_vendor_id('lscpu')
    elif _linuxutil.is_procinfo_available():
        return libcpu.linux_get_cpu_vendor_id('proc')
    else:
        return 'Not detected'
