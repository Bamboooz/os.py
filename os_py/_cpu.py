import psutil
import cpuinfo


def cpu_model():
    return cpuinfo.get_cpu_info()['brand_raw']


def cpu_physical_cores():
    return psutil.cpu_count(logical=False)


def cpu_logical_cores():
    return psutil.cpu_count(logical=True) - psutil.cpu_count(logical=False)


def cpu_total_cores():
    return psutil.cpu_count(logical=True)


def cpu_clockspeed():
    return cpuinfo.get_cpu_info()['hz_actual_friendly']


def cpu_architecture():
    return cpuinfo.get_cpu_info()['arch']


def cpu_usage():
    return str(psutil.cpu_percent()) + '%'


def cpu_vendor_id():
    return cpuinfo.get_cpu_info()['vendor_id_raw']
