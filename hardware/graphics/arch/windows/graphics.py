# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import platform
import subprocess


def execute_command(command, trim):
    result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.DEVNULL)
    lines = result.split('\n')

    if 0 < trim <= len(lines):
        lines = lines[trim:]

    lines = [line for line in lines if line.strip()]  # Remove empty lines

    output = '\n'.join(lines)
    return output


def get_nvidia_smi() -> str:
    if platform.system() == 'Windows':
        n_smi = execute_command("where nvidia-smi", 0)
    else:
        n_smi = "nvidia-smi"

    return n_smi


def ids() -> list:
    output = execute_command(f'{get_nvidia_smi()} --query-gpu=index --format=csv,noheader,nounits', 0)
    gpu_ids = [int(gpu_id.strip()) for gpu_id in output.strip().split('\n')]
    return gpu_ids


def uuid(num) -> str:
    output = execute_command(f'{get_nvidia_smi()} --query-gpu=uuid --id={num} --format=csv,noheader,nounits', 0)
    gpu_uuid = output.strip()
    return gpu_uuid


def m_total(num) -> float:
    output = execute_command(f'{get_nvidia_smi()} --query-gpu=memory.total --id={num} --format=csv,noheader,nounits', 0)
    gpu_memory_total = int(output.strip())
    return gpu_memory_total


def m_free(num) -> float:
    output = execute_command(f'{get_nvidia_smi()} --query-gpu=memory.free --id={num} --format=csv,noheader,nounits', 0)
    gpu_memory_free = int(output.strip())
    return gpu_memory_free


def m_used(num) -> float:
    total = m_total(num)
    free = m_free(num)
    return total - free


def model(num) -> str:
    output = execute_command(f'{get_nvidia_smi()} --query-gpu=name --id={num} --format=csv,noheader,nounits', 0)
    gpu_name = output.strip()
    return gpu_name


def serial(num) -> str:
    output = execute_command(f'{get_nvidia_smi()} --query-gpu=gpu_serial --id={num} --format=csv,noheader,nounits', 0)
    gpu_serial_number = output.strip()
    return gpu_serial_number


def mode(num) -> str:
    output = execute_command(f'{get_nvidia_smi()} --query-gpu=display_mode --id={num} --format=csv,noheader,nounits', 0)
    gpu_display_mode = output.strip()
    return gpu_display_mode


def active(num) -> str:
    output = execute_command(f'{get_nvidia_smi()} --query-gpu=display_active --id={num} --format=csv,noheader,nounits', 0)
    gpu_display_active = output.strip()
    return gpu_display_active
