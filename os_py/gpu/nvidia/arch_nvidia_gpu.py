import os_py.gpu.nvidia.nvidia_smi as gpu


def gpu_id():
    return gpu.get_gpu_info()['gpu_id']


def gpu_name():
    return gpu.get_gpu_info()['gpu_name']


def gpu_serial_number():
    return gpu.get_gpu_info()['gpu_serial_number']


def gpu_uuid():
    return gpu.get_gpu_info()['gpu_uuid']


def gpu_memory_total():
    return gpu.get_gpu_info()['gpu_memory_total']


def gpu_memory_free():
    return gpu.get_gpu_info()['gpu_memory_free']


def gpu_memory_used():
    return gpu.get_gpu_info()['gpu_memory_used']


def gpu_display_mode():
    return gpu.get_gpu_info()['gpu_display_mode']


def gpu_display_active():
    return gpu.get_gpu_info()['gpu_display_active']
