# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import subprocess
import os
import platform


def _get_nvidia_smi():
    """
    Returns the path to the nvidia-smi executable.

    On Windows, the function looks for nvidia-smi in the PATH environment variable.
    If nvidia-smi is not found in the PATH, it looks for it in the default installation
    directory. On other platforms, the function assumes that nvidia-smi is in the PATH.
    """
    if platform.system() == "Windows":
        nvidia_smi = subprocess.check_output(["where", "nvidia-smi"]).decode().strip()

        if not nvidia_smi:
            return os.path.join(os.environ['systemdrive'], "Program Files", "NVIDIA Corporation", "NVSMI", "nvidia-smi.exe")

    return "nvidia-smi"  # on linux nvidia-smi is simply accessed by nvidia-smi command

def nvidia_smi_get_gpu_info():
    """
    Returns information about the NVIDIA GPUs installed on the system.
    The function calls the nvidia-smi command-line tool and extracts GPU information.
    """
    output = subprocess.check_output([_get_nvidia_smi(), "--query-gpu=index,uuid,memory.total,memory.used,name,gpu_serial,display_active,display_mode", "--format=csv,noheader,nounits"], universal_newlines=True)

    gpu_info = {}

    for line in output.strip().split('\n'):
        values = line.strip().split(', ')

        gpu_info[int(values[0])] = {
            'gpu_id': int(values[0]),
            'gpu_uuid': values[1],
            'gpu_memory_total': int(values[2]),
            'gpu_memory_free': int(values[2]) - int(values[3]),
            'gpu_memory_used': int(values[3]),
            'gpu_name': values[4],
            'gpu_serial_number': values[5],
            'gpu_display_mode': values[6],
            'gpu_display_active': values[7],
        }
    return gpu_info
