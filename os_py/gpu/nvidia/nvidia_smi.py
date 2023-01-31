from subprocess import Popen, PIPE
from distutils import spawn
import os
import math
import random
import time
import platform


class GPU:
    def __init__(self, ID, uuid, load, memoryTotal, memoryUsed, memoryFree, driver, gpu_name, serial, display_mode,
                 display_active, temp_gpu):
        self.id = ID
        self.uuid = uuid
        self.load = load
        self.memoryUtil = float(memoryUsed) / float(memoryTotal)
        self.memoryTotal = memoryTotal
        self.memoryUsed = memoryUsed
        self.memoryFree = memoryFree
        self.driver = driver
        self.name = gpu_name
        self.serial = serial
        self.display_mode = display_mode
        self.display_active = display_active
        self.temperature = temp_gpu


def safe_float_cast(strNumber):
    try:
        number = float(strNumber)
    except ValueError:
        number = float('nan')
    return number


def get_gpus():
    if platform.system() == "Windows":
        nvidia_smi = spawn.find_executable('nvidia-smi')  # Finding nvidia-smi on Windows
        if nvidia_smi is None:  # If not found, try to find other location of nvidia-smi
            nvidia_smi = "%s\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe" % os.environ['systemdrive']
    else:
        nvidia_smi = "nvidia-smi"

    # Get ID, processing and memory utilization for all GPUs
    try:
        p = Popen([nvidia_smi,
                   "--query-gpu=index,uuid,utilization.gpu,memory.total,memory.used,memory.free,driver_version,name,gpu_serial,display_active,display_mode,temperature.gpu",
                   "--format=csv,noheader,nounits"], stdout=PIPE)
        stdout, std_error = p.communicate()
    except Exception:
        return []

    output = stdout.decode('UTF-8')  # output = output[2:-1] # Remove b' and ' from string added by python
    lines = output.split(os.linesep)
    numDevices = len(lines) - 1
    GPUs = []

    for g in range(numDevices):
        line = lines[g]
        vals = line.split(', ')
        for i in range(12):
            if i == 0:
                deviceIds = int(vals[i])
            elif i == 1:
                uuid = vals[i]
            elif i == 2:
                gpuUtil = safe_float_cast(vals[i]) / 100
            elif i == 3:
                memTotal = safe_float_cast(vals[i])
            elif i == 4:
                memUsed = safe_float_cast(vals[i])
            elif i == 5:
                memFree = safe_float_cast(vals[i])
            elif i == 6:
                driver = vals[i]
            elif i == 7:
                gpu_name = vals[i]
            elif i == 8:
                serial = vals[i]
            elif i == 9:
                display_active = vals[i]
            elif i == 10:
                display_mode = vals[i]
            elif i == 11:
                temp_gpu = safe_float_cast(vals[i]);
        GPUs.append(GPU(deviceIds, uuid, gpuUtil, memTotal, memUsed, memFree, driver, gpu_name, serial, display_mode,
                        display_active, temp_gpu))
    return GPUs  # (deviceIds, gpuUtil, memUtil)


def get_available(order='first', limit=1, maxLoad=0.5, maxMemory=0.5, memoryFree=0, includeNan=False, excludeID=None,
                  excludeUUID=None):
    # order = first | last | random | load | memory
    # first --> select the GPU with the lowest ID (DEFAULT)
    # last --> select the GPU with the highest ID
    # random --> select a random available GPU
    # load --> select the GPU with the lowest load
    # memory --> select the GPU with the most memory available
    # limit = 1 (DEFAULT), 2, ..., Inf
    # Limit sets the upper limit for the number of GPUs to return. E.g. if limit = 2, but only one is available, only one is returned.

    # Get device IDs, load and memory usage
    if excludeUUID is None:
        excludeUUID = []
    if excludeID is None:
        excludeID = []
    GPUs = get_gpus()

    # Determine, which GPUs are available
    gpu_availability = get_availability(GPUs, maxLoad=maxLoad, maxMemory=maxMemory, memoryFree=memoryFree,
                                        includeNan=includeNan, excludeID=excludeID, excludeUUID=excludeUUID)
    available_gpu_index = [idx for idx in range(0, len(gpu_availability)) if (gpu_availability[idx] == 1)]
    # Discard unavailable GPUs
    GPUs = [GPUs[g] for g in available_gpu_index]

    # Sort available GPUs according to the order argument
    if order == 'first':
        GPUs.sort(key=lambda x: float('inf') if math.isnan(x.id) else x.id, reverse=False)
    elif order == 'last':
        GPUs.sort(key=lambda x: float('-inf') if math.isnan(x.id) else x.id, reverse=True)
    elif order == 'random':
        GPUs = [GPUs[g] for g in random.sample(range(0, len(GPUs)), len(GPUs))]
    elif order == 'load':
        GPUs.sort(key=lambda x: float('inf') if math.isnan(x.load) else x.load, reverse=False)
    elif order == 'memory':
        GPUs.sort(key=lambda x: float('inf') if math.isnan(x.memoryUtil) else x.memoryUtil, reverse=False)

    # Extract the number of desired GPUs, but limited to the total number of available GPUs
    GPUs = GPUs[0:min(limit, len(GPUs))]

    # Extract the device IDs from the GPUs and return them
    deviceIds = [gpu.id for gpu in GPUs]

    return deviceIds


def get_availability(GPUs, maxLoad=0.5, maxMemory=0.5, memoryFree=0, includeNan=False, excludeID=[], excludeUUID=[]):
    # Determine, which GPUs are available
    gpu_availability = [
        1 if (gpu.memoryFree >= memoryFree) and (gpu.load < maxLoad or (includeNan and math.isnan(gpu.load))) and (
                gpu.memoryUtil < maxMemory or (includeNan and math.isnan(gpu.memoryUtil))) and (
                     (gpu.id not in excludeID) and (gpu.uuid not in excludeUUID)) else 0 for gpu in GPUs]
    return gpu_availability


def get_first_available(order='first', maxLoad=0.5, maxMemory=0.5, attempts=1, interval=900, verbose=False,
                        includeNan=False, excludeID=None, excludeUUID=None):
    global available
    if excludeUUID is None:
        excludeUUID = []
    if excludeID is None:
        excludeID = []

    for i in range(attempts):
        if verbose:
            print('Attempting (' + str(i + 1) + '/' + str(attempts) + ') to locate available GPU.')
        # Get first available GPU
        available = get_available(order=order, limit=1, maxLoad=maxLoad, maxMemory=maxMemory, includeNan=includeNan,
                                  excludeID=excludeID, excludeUUID=excludeUUID)
        # If an available GPU was found, break for loop.
        if available:
            if verbose:
                print('GPU ' + str(available) + ' located!')
            break
        # If this is not the last attempt, sleep for 'interval' seconds
        if i != attempts - 1:
            time.sleep(interval)
    # Check if an GPU was found, or if the attempts simply ran out. Throw error, if no GPU was found
    if not available:
        raise RuntimeError('Could not find an available GPU after ' + str(attempts) + ' attempts with ' + str(
            interval) + ' seconds interval.')

    # Return found GPU
    return available


def get_gpu_info():
    GPUs = get_gpus()
    for gpu in GPUs:
        return {
            'gpu_id': gpu.id,
            'gpu_name': gpu.name,
            'gpu_serial_number': gpu.serial,
            'gpu_uuid': gpu.uuid,
            'gpu_memory_total': str(gpu.memoryTotal) + 'MB',
            'gpu_memory_free': str(gpu.memoryFree) + 'MB',
            'gpu_memory_used': str(gpu.memoryUsed) + 'MB',
            'gpu_display_mode': gpu.display_mode,
            'gpu_display_active': gpu.display_active
        }
