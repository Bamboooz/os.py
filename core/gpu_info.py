import sys
import GPUtil
from core.exception import *


gpus = GPUtil.getGPUs()


def gpu_id():
    if sys.platform == 'win32':
        for gpu in gpus:
            return gpu.id
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def gpu_name():
    if sys.platform == 'win32':
        for gpu in gpus:
            return gpu.name
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def gpu_load():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.load*100}%"
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def gpu_free_memory():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.memoryFree}MB"
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def gpu_used_memory():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.memoryUsed}MB"
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def gpu_total_memory():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.memoryTotal}MB"
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def gpu_temperature():
    if sys.platform == 'win32':
        gpu = GPUtil.getGPUs()[0]
        return str(gpu.temperature) + 'C'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def gpu_uuid():
    if sys.platform == 'win32':
        for gpu in gpus:
            return gpu.uuid
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()
