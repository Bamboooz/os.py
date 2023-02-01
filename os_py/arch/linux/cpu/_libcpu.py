import multiprocessing
import platform
import subprocess


def linux_get_cpu_model(method='lscpu'):
    def linux_lscpu_model():
        ls_cpu_output = subprocess.getoutput('lscpu').strip().splitlines()
        for item in ls_cpu_output:
            if item.startswith('Model name:'):
                return item.replace('Model name:', '').strip()

    def linux_proc_cpuinfo_model():
        ls_cpu_output = subprocess.getoutput('cat /proc/cpuinfo').strip().splitlines()
        for item in ls_cpu_output:
            if item.startswith('model name'):
                return item.replace('model name', '').replace(':', '').strip()

    if method == 'lscpu':
        return linux_lscpu_model()
    elif method == 'proc':
        return linux_proc_cpuinfo_model()


def linux_get_cpu_total_cores():
    return multiprocessing.cpu_count()


def linux_get_cpu_clockspeed(method='proc'):
    def linux_proc_cpuinfo_clockspeed():
        ls_cpu_output = subprocess.getoutput('cat /proc/cpuinfo').strip().splitlines()
        for item in ls_cpu_output:
            if item.startswith('cpu MHz'):
                return str(int(round(float(item.replace('cpu MHz', '').replace(':', '').strip())))) + 'MHz'

    if method == 'proc':
        return linux_proc_cpuinfo_clockspeed()


def linux_get_cpu_architecture():
    return platform.machine()


def linux_get_cpu_bits():
    return platform.architecture()[0]


def linux_get_cpu_manufacturer(method='lscpu'):
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
    }[linux_get_cpu_vendor_id(method).lower()]


def linux_get_cpu_vendor_id(method='proc'):
    def linux_lscpu_vendor_id():
        ls_cpu_output = subprocess.getoutput('lscpu').strip().splitlines()
        for item in ls_cpu_output:
            if item.startswith('Vendor ID:'):
                return item.replace('Vendor ID:', '').strip()

    def linux_proc_cpuinfo_vendor_id():
        ls_cpu_output = subprocess.getoutput('cat /proc/cpuinfo').strip().splitlines()
        for item in ls_cpu_output:
            if item.startswith('vendor_id'):
                return item.replace('vendor_id', '').replace(':', '').strip()

    if method == 'lscpu':
        return linux_lscpu_vendor_id()
    elif method == 'proc':
        return linux_proc_cpuinfo_vendor_id()
