import sys
import GPUtil
from core.exception import *


gpus = GPUtil.getGPUs()


def gpu_id():
    if sys.platform == 'win32':
        for gpu in gpus:
            return gpu.id
    else:
        return unsupported_exception()


def gpu_name():
    if sys.platform == 'win32':
        for gpu in gpus:
            return gpu.name
    else:
        return unsupported_exception()


def gpu_load():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.load*100}%"
    else:
        return unsupported_exception()


def gpu_free_memory():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.memoryFree}MB"
    else:
        return unsupported_exception()


def gpu_used_memory():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.memoryUsed}MB"
    else:
        return unsupported_exception()


def gpu_total_memory():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.memoryTotal}MB"
    else:
        return unsupported_exception()


def gpu_temperature():
    if sys.platform == 'win32':
        gpu = GPUtil.getGPUs()[0]
        return str(gpu.temperature) + 'C'
    else:
        return unsupported_exception()
