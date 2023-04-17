# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# this file is responsible for choosing method of information retrieval


from os_py.arch.windows import processor as win_processor
from os_py.arch.windows import device as win_device
from os_py.arch.windows import machine as win_machine
from os_py.arch.windows import storage as win_storage
from os_py.arch.windows import motherboard as win_motherboard


class processor:
    @staticmethod
    def get_cpu_model():
        """
        Tries to get the CPU model using WMIC, and if that fails, tries to get it using the Windows registry.

        Returns:
            - The CPU model, or None if it cannot be obtained.
        """
        try:
            return win_processor.wmic_get_cpu_model()
        except:
            try:
                return win_processor.winreg_get_cpu_model()
            except:
                return None

    @staticmethod
    def get_cpu_clockspeed():
        """
        Tries to get the CPU clockspeed using WMIC, and if that fails, tries to get it using the Windows registry.

        Returns:
            - The CPU clockspeed, or None if it cannot be obtained.
        """
        try:
            return win_processor.wmic_get_cpu_clockspeed()
        except:
            try:
                return win_processor.winreg_get_cpu_clockspeed()
            except:
                return None

    @staticmethod
    def get_cpu_total_cores():
        """
        Tries to get the total number of CPU cores using multiprocessing.

        Returns:
            - The total number of CPU cores, or None if it cannot be obtained.
        """
        try:
            return win_processor.multiprocessing_get_cpu_total_cores()
        except:
            return None

    @staticmethod
    def get_cpu_architecture():
        """
        Tries to get the CPU architecture using the platform module, and if that fails, tries to get it using WMIC or
        the Windows registry.

        Returns:
            - The CPU architecture, or None if it cannot be obtained.
        """
        try:
            return win_processor.platform_get_cpu_architecture()
        except:
            try:
                return win_processor.wmic_get_cpu_architecture()
            except:
                try:
                    return win_processor.winreg_get_cpu_architecture()
                except:
                    return None


    @staticmethod
    def get_cpu_vendor_id():
        """
        Tries to get the CPU vendor ID using WMIC, and if that fails, tries to get it using the Windows registry.

        Returns:
            - The CPU vendor ID, or None if it cannot be obtained.
        """
        try:
            return win_processor.wmic_get_cpu_vendor_id()
        except:
            try:
                return win_processor.winreg_get_cpu_vendor_id()
            except:
                return None

    @staticmethod
    def get_cpu_manufacturer():
        """
        Tries to get the CPU manufacturer using WMIC, and if that fails, tries to get it using the Windows registry.

        Returns:
            - The CPU manufacturer, or None if it cannot be obtained.
        """
        try:
            return win_processor.wmic_get_cpu_manufacturer()
        except:
            try:
                return win_processor.winreg_get_cpu_manufacturer()
            except:
                return None


class machine:
    @staticmethod
    def get_firmware_type():
        """
        Attempts to determine the firmware type of the machine using several different methods.

        Returns:
            - A string representing the firmware type, such as 'BIOS' or 'UEFI', if successful.
            - None if unable to determine the firmware type using any of the methods.
        """
        try:
            return win_machine.setupact_get_firmware_type()
        except:
            try:
                return win_machine.powershell_get_firmware_type()
            except:
                try:
                    return win_machine.winreg_get_firmware_type()
                except:
                    try:
                        return win_machine.ctypes_kernel32_get_firmware_type()
                    except:
                        return None


class motherboard:
    @staticmethod
    def get_motherboard_product():
        """
        Attempts to obtain the product name of the motherboard using two different methods.

        Returns:
            - A string representing the product name of the motherboard if successful.
            - None if unable to obtain the product name using any of the methods.
        """
        try:
            return win_motherboard.wmic_get_motherboard_product()
        except:
            try:
                return win_motherboard.winreg_get_motherboard_product()
            except:
                return None

    @staticmethod
    def get_motherboard_manufacturer():
        """
        Attempts to obtain the manufacturer name of the motherboard using two different methods.

        Returns:
            - A string representing the manufacturer name of the motherboard if successful.
            - None if unable to obtain the manufacturer name using any of the methods.
        """
        try:
            return win_motherboard.wmic_get_motherboard_manufacturer()
        except:
            try:
                return win_motherboard.winreg_get_motherboard_manufacturer()
            except:
                return None

    @staticmethod
    def get_motherboard_version():
        """
        Attempts to obtain the version number of the motherboard using two different methods.

        Returns:
            - A string representing the version number of the motherboard if successful.
            - None if unable to obtain the version number using any of the methods.
        """
        try:
            return win_motherboard.wmic_get_motherboard_version()
        except:
            try:
                return win_motherboard.winreg_get_motherboard_version()
            except:
                return None


class device:
    @staticmethod
    def get_number_of_external_drives():
        """
        Attempts to retrieve the number of external drives on a Windows device using either the "wmic" command or PowerShell.

        Returns:
        - an integer representing the number of external drives on the device, if successful.
        - None if the attempt(s) to retrieve the number of external drives fail.
        """
        try:
            return win_device.wmic_get_number_of_external_drives()
        except:
            try:
                return win_device.powershell_get_number_of_external_drives()
            except:
                return None

    @staticmethod
    def get_external_drives():
        """
        Attempts to retrieve information about the external drives on a Windows device using either the "wmic" command or PowerShell.

        Returns:
            - a data structure (such as a list or dictionary) representing the external drives and their properties, if successful.
            - None if the attempt(s) to retrieve the external drive information fail.
        """
        try:
            return win_device.wmic_get_external_drives()
        except:
            try:
                return win_device.powershell_get_external_drives()
            except:
                return None


class storage:
    @staticmethod
    def get_drive_list():
        """
        This method returns a list of available drives on the system

        Returns:
            - A list of available drive letters
        """
        try:
            return win_storage.os_path_drive_list()
        except:
            try:
                return win_storage.ctypes_windll_drive_list()
            except:
                return None


    @staticmethod
    def get_disk_total_space(drive=''):
        """
        This method returns the total space of a specified drive

        Args:
            - drive: the drive letter of the drive to get the total space of

        Returns:
            - The total space of the drive in gigabytes
        """
        try:
            return win_storage.shutil_disk_total_space(drive)
        except:
            try:
                return win_storage.ctypes_windll_get_total_space(drive)
            except:
                return None


    @staticmethod
    def get_disk_used_space(drive=''):
        """
        This method returns the used space of a specified drive

        Args:
            - drive: the drive letter of the drive to get the used space of

        Returns:
            - The used space of the drive in gigabytes
        """
        try:
            return win_storage.shutil_disk_used_space(drive)
        except:
            try:
                return win_storage.ctypes_windll_get_used_space(drive)
            except:
                return None


    @staticmethod
    def get_disk_free_space(drive=''):
        """
        This method returns the free space of a specified drive

        Args:
            - drive: the drive letter of the drive to get the free space of

        Returns:
            - The free space of the drive in gigabytes
        """
        try:
            return win_storage.shutil_disk_free_space(drive)
        except:
            try:
                return win_storage.ctypes_windll_get_free_space(drive)
            except:
                return None


    @staticmethod
    def get_disk_used_space_percent(drive=''):
        """
        This method returns the percentage of used space of a specified drive

        Args:
            - drive: the drive letter of the drive to get the used space percentage of

        Returns:
            - The percentage of used space of the drive as a float value
        """
        try:
            return win_storage.shutil_disk_used_space_percent(drive)
        except:
            try:
                return win_storage.ctypes_windll_get_used_space_percent(drive)
            except:
                return None
