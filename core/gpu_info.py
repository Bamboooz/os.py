import sys
import GPUtil
import os
from core.exception import *


gpus = GPUtil.getGPUs()


def gpu_id():
    if sys.platform == 'win32':
        for gpu in gpus:
            return gpu.id
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        data = os.popen('lshw -C display').read()
        for line in str(data).splitlines():
            if 'physical id' in line:
                return line.replace('physical id: ', '').replace('       ', '')
    else:
        print(unsupported_exception())


def gpu_name():
    if sys.platform == 'win32':
        for gpu in gpus:
            return gpu.name
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        data = os.popen('lshw -C display').read()
        for line in str(data).splitlines():
            if 'product: ' in line:
                return line.replace('product: ', '').replace('       ', '')
    else:
        print(unsupported_exception())


def gpu_load():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.load*100}%"
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        print(feature_not_implemented_yet())
    else:
        print(unsupported_exception())


def gpu_free_memory():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.memoryFree}MB"
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        print(feature_not_implemented_yet())
    else:
        print(unsupported_exception())


def gpu_used_memory():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.memoryUsed}MB"
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        print(feature_not_implemented_yet())
    else:
        print(unsupported_exception())


def gpu_total_memory():
    if sys.platform == 'win32':
        for gpu in gpus:
            return f"{gpu.memoryTotal}MB"
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        print(feature_not_implemented_yet())
    else:
        print(unsupported_exception())


def gpu_temperature():
    if sys.platform == 'win32':
        gpu = GPUtil.getGPUs()[0]
        return str(gpu.temperature) + 'C'
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        print(feature_not_implemented_yet())
    else:
        print(unsupported_exception())
