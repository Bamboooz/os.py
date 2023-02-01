from subprocess import Popen, PIPE
from distutils import spawn
import os
import platform


def safe_float_cast(strNumber):
    try:
        number = float(strNumber)
    except ValueError:
        number = float('nan')
    return number


def get_nvidia_smi():
    if platform.system() == "Windows":
        nvidia_smi = spawn.find_executable('nvidia-smi')  # Finding nvidia-smi on Windows

        if nvidia_smi is None:  # If not found, try to find other location of nvidia-smi
            nvidia_smi = "%s\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe" % os.environ['systemdrive']

        return nvidia_smi
    else:
        return "nvidia-smi"


def get_gpu_info():
    # Get ID, processing and memory utilization for all GPUs
    try:
        p = Popen([get_nvidia_smi(), "--query-gpu=index,uuid,memory.total,memory.used,name,gpu_serial,display_active,display_mode", "--format=csv,noheader,nounits"], stdout=PIPE)
        stdout, std_error = p.communicate()
        output = stdout.decode('UTF-8')
    except Exception:
        raise Exception("Could not detect connected gpu's")

    return {
        'gpu_id': output.split(', ')[0].strip(),
        'gpu_name': output.split(', ')[4].strip(),
        'gpu_serial_number': output.split(', ')[5].strip(),
        'gpu_uuid': output.split(', ')[1].strip(),
        'gpu_memory_total': output.split(', ')[2] + 'MB'.strip(),
        'gpu_memory_free': str(int(output.split(', ')[2]) - int(output.split(', ')[3])) + 'MB'.strip(),
        'gpu_memory_used': output.split(', ')[3] + 'MB'.strip(),
        'gpu_display_mode': output.split(', ')[6].strip(),
        'gpu_display_active': output.split(', ')[7].strip()
    }
