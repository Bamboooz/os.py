# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import datetime
import platform

# import shared modules
from os_py.shared import gpu as _gpu
from os_py.shared import sys as _sys

# import Windows modules
from os_py.os_py_windows import processor as _win_proc
from os_py.os_py_windows import device as _win_device
from os_py.os_py_windows import machine as _win_machine
from os_py.os_py_windows import storage as _win_storage
from os_py.os_py_windows import motherboard as _win_board
from os_py.arch.windows import memory as _win_ram

# import registry module
from os_py.registry import winreg as _winreg


__version__ = '0.0.1'


class sys:
    def __init__(self):  # raise exception if the operating system if unsupported
        if platform.system().lower() != 'windows': raise Exception('Error: Unsupported operating system.')

    @staticmethod
    def get_os_info():
        """
        Returns a dictionary containing information about the installed operating system.

        Returns:
            A dictionary containing information about the installed operating system.
            If any of the information cannot be obtained, its value in the dictionary will be None.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        return {
            "name": _sys.os_name(),
            "hostname": _sys.machine_hostname(),
            "version": _sys.os_version(),
            "platform": _sys.os_platform(),
            "release": _sys.os_release(),
            "arch": _sys.os_architecture()
        }


class cpu:
    def __init__(self):  # raise exception if the operating system if unsupported
        if platform.system().lower() != 'windows': raise Exception('Error: Unsupported operating system.')

    @staticmethod
    def get_processor_info():
        """
        Gets information about the CPU, and return it in a form of a dictionary.

        Returns:
            A dictionary containing information about the CPU.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        return {
            "model": _win_proc.get_cpu_model(),
            "clockspeed": _win_proc.get_cpu_clockspeed(),
            "total_cores": _win_proc.get_cpu_total_cores(),
            "arch": _win_proc.get_cpu_architecture(),
            "vendor_id": _win_proc.get_cpu_vendor_id(),
            "manufacturer": _win_proc.get_cpu_manufacturer()
        }


class gpu:
    def __init__(self):  # raise exception if the operating system if unsupported
        if platform.system().lower() != 'widows': raise Exception('Error: Unsupported operating system.')

        try:  # checking if installed GPU is made by NVIDIA
            _gpu.nvidia_smi_get_gpu_info()
        except:
            raise Exception("Error: os.py supports only nvidia GPU's.")

    @staticmethod
    def get_graphics_card_info(index=None):
        """
        Returns a dictionary containing information about the installed GPU's.

        Returns:
            A dictionary containing information about the installed GPU's.
            If any of the information cannot be obtained, its value in the dictionary will be None.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        if index is None:
            return _gpu.nvidia_smi_get_gpu_info()
        else:
            return _gpu.nvidia_smi_get_gpu_info()[index]


class memory:
    def __init__(self):  # raise exception if the operating system if unsupported
        if platform.system().lower() != 'windows': raise Exception('Error: Unsupported operating system.')

    @staticmethod
    def get_ram_info():
        """
        Returns a dictionary containing information about the installed RAM memory.

        Returns:
            A dictionary containing information about the installed RAM memory.
            If any of the information cannot be obtained, its value in the dictionary will be None.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        return {
            "capacity": _win_ram.wmic_get_ram_capacity(),
            "number_of_sticks": _win_ram.wmic_get_ram_sticks_number(),
            "form_factor": _win_ram.wmic_get_ram_form_factor(),
            "type": _win_ram.wmic_get_ram_memory_type(),
            "manufacturer": _win_ram.wmic_get_ram_manufacturer(),
            "clockspeed": _win_ram.wmic_get_ram_clockspeed(),
            "serial_number": _win_ram.wmic_get_ram_serial_number()
        }


class storage:
    def __init__(self):  # raise exception if the operating system if unsupported
        if platform.system().lower() != 'windows': raise Exception('Error: Unsupported operating system.')

    @staticmethod
    def get_drive_list():
        """
        Returns a list of drives installed on your device.

        Returns:
            Returns a list of drives installed on your device.
            If any of the information cannot be obtained, its value in the dictionary will be None.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        return _win_storage.get_drive_list()

    @staticmethod
    def get_drive_info(drive=''):
        """
        Returns a dictionary containing information about the machine's storage.

        Returns:
            A dictionary containing information about the installed storage (total, used, free memory etc.)
            If any of the information cannot be obtained, its value in the dictionary will be None.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        return {
            "total": _win_storage.get_disk_total_space(drive),
            "used": _win_storage.get_disk_free_space(drive),
            "free": _win_storage.get_disk_free_space(drive),
            "used_percent": _win_storage.get_disk_used_space_percent(drive)
        }


class motherboard:
    def __init__(self):  # raise exception if the operating system if unsupported
        if platform.system().lower() != 'windows': raise Exception('Error: Unsupported operating system.')

    @staticmethod
    def get_motherboard_info():
        """
        Returns a dictionary containing information about the motherboard of the machine.

        Returns:
            A dictionary containing information about the installed motherboard.
            If any of the information cannot be obtained, its value in the dictionary will be None.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        return {
            "model": _win_board.get_motherboard_product(),
            "manufacturer": _win_board.get_motherboard_manufacturer(),
            "version": _win_board.get_motherboard_version()
        }


class device:
    def __init__(self):  # raise exception if the operating system if unsupported
        if platform.system().lower() != 'windows': raise Exception('Error: Unsupported operating system.')

    @staticmethod
    def get_number_of_external_drives():
        """
        Attempts to retrieve the number of external drives on a Windows device using either the WMI client or PowerShell.

        Returns:
            An integer representing the number of external drives on the device, if successful.
            None if the attempt(s) to retrieve the number of external drives fail.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        return _win_device.get_number_of_external_drives()

    @staticmethod
    def get_external_drives():
        """
        Attempts to retrieve information about the external drives on a Windows device using either the "wmic" command or PowerShell.

        Returns:
            List representing the external drives and letters assigned to them.
            None if the attempt(s) to retrieve the external drive information fail.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        return _win_device.get_external_drives()


class machine:
    def __init__(self):  # raise exception if the operating system if unsupported
        if platform.system().lower() != 'windows': raise Exception('Error: Unsupported operating system.')

    @staticmethod
    def get_firmware_type():
        """
        Attempts to retrieve machine's firmware type (BIOS/UEFI) using different methods such as setupact, Windows registry etc.

        Returns:
            The machines firmware type (BIOS/UEFI).
            None if the attempt(s) to retrieve the external drive information fail.

        For more information visit: https://github.com/Bamboooz/os.py/wiki
        """
        return _win_machine.get_firmware_type()
