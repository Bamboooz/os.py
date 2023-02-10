import platform
import subprocess

from collections import defaultdict

from scripts._common import Handler
from os_py import _battery, _inet, _machine, _sys, _storage
from os_py.gpu.nvidia import arch_nvidia_gpu as nvidia

from os_py.arch.linux import ldistro

from os_py.arch.linux import machine as lmach
from os_py.arch.linux import device as ldev
from os_py.arch.linux import sound as lso
from os_py.arch.linux import motherboard as lmb
from os_py.arch.win32.cpu import arch_win32_cpu as wincpu
from os_py.arch.win32.ram import arch_win32_ram as winram

from os_py.arch.win32 import machine as wmach
from os_py.arch.win32 import device as wdev
from os_py.arch.win32 import sound as wso
from os_py.arch.win32 import motherboard as wmb
from os_py.arch.linux.cpu import arch_linux_cpu as linuxcpu
from os_py.arch.linux.ram import arch_linux_ram as linuxram


class system:  # access for system functions from library
    @staticmethod
    def os_name():
        """
            Returns operating system's name e.g. Windows, Linux etc.
        """
        fun = {
            'windows': _sys.os_name,
            'linux': _sys.os_name
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def os_version():
        """
            Returns operating system's version e.g. 10.0.19045
        """
        fun = {
            'windows': _sys.os_version,
            'linux': _sys.os_version
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def os_platform():
        """
            Returns a single string identifying the underlying platform
        """
        fun = {
            'windows': _sys.os_name,
            'linux': _sys.os_platform
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def os_release():
        """
            Detects your operating system's release e.g. Windows 10
        """
        fun = {
            'windows': _sys.os_release,
            'linux': _sys.os_release
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def os_architecture():
        """
            Detects operating systems architecture e.g. 32-bit or 64-bit
        """
        fun = {
            'windows': _sys.os_architecture,
            'linux': _sys.os_architecture
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def machine_architecture():
        """
            Detects machines architecture e.g. AMD64
        """
        fun = {
            'windows': _sys.machine_architecture,
            'linux': _sys.machine_architecture
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def linux_distro():
        """
            Detects specific distributions on Linux-based systems
        """
        fun = {
            'windows': lambda: Handler.exception("Windows operating systems don't have distibutions"),
            'linux': ldistro.linux_distro
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()


class cpu:
    @staticmethod
    def cpu_model():
        """
            Detects CPU model eg. AMD Ryzen 7 4800H
        """
        fun = {
            'windows': wincpu.win32_get_cpu_model,
            'linux': linuxcpu.linux_get_cpu_model
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def cpu_total_cores():
        """
            Returns total number of your CPU's cores
        """
        fun = {
            'windows': wincpu.win32_get_cpu_total_cores,
            'linux': linuxcpu.linux_get_cpu_total_cores
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def cpu_clockspeed():
        """
            Detects CPU clockspeed
        """
        fun = {
            'windows': wincpu.win32_get_cpu_clockspeed,
            'linux': linuxcpu.linux_get_cpu_clockspeed
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def cpu_architecture():
        """
            Returns your processors architecture: e.g. AMD64
        """
        fun = {
            'windows': wincpu.win32_get_cpu_architecture,
            'linux': linuxcpu.linux_get_cpu_architecture
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def cpu_bits():
        """
            Detects CPU's bit count e.g. 64bit
        """
        fun = {
            'windows': wincpu.win32_get_cpu_bits,
            'linux': linuxcpu.linux_get_cpu_bits
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def cpu_manufacturer():
        """
            Returns your processors manufacturer e.g.: AMD
        """
        fun = {
            'windows': wincpu.win32_get_cpu_manufacturer,
            'linux': linuxcpu.linux_get_cpu_manufacturer
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def cpu_vendor_id():
        """
            Detects your CPU's vendor id e.g.: AuthenticAMD
        """
        fun = {
            'windows': wincpu.win32_get_cpu_vendor_id,
            'linux': linuxcpu.linux_get_cpu_vendor_id
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()


class gpu:
    def __init__(self):
        try:
            subprocess.getoutput('nvidia-smi')
            self.gpu_manufacturer = 'nvidia'
        except:
            self.gpu_manufacturer = 'amd'

    def gpu_id(self):
        """
            Detects your GPU's id (main GPU is 1, next one is 2 and so on)
        """
        fun = {
            'nvidia': nvidia.gpu_id,
            'amd': lambda: Handler.exception("Error: Currently os.py does not support AMD GPU's.")
        }.get(self.gpu_manufacturer, lambda: Handler.exception("Unsupported platform"))
        return fun()

    def gpu_name(self):
        """
            Retrieves your GPU's model e.g.: NVIDIA GTX 1660 Ti
        """
        fun = {
            'nvidia': nvidia.gpu_name,
            'amd': lambda: Handler.exception("Error: Currently os.py does not support AMD GPU's.")
        }.get(self.gpu_manufacturer, lambda: Handler.exception("Unsupported platform"))
        return fun()

    def gpu_serial_number(self):
        """
            Returns your GPU's serial number
        """
        fun = {
            'nvidia': nvidia.gpu_serial_number,
            'amd': lambda: Handler.exception("Error: Currently os.py does not support AMD GPU's.")
        }.get(self.gpu_manufacturer, lambda: Handler.exception("Unsupported platform"))
        return fun()

    def gpu_uuid(self):
        """
            Returns your GPU's uuid
        """
        fun = {
            'nvidia': nvidia.gpu_uuid,
            'amd': lambda: Handler.exception("Error: Currently os.py does not support AMD GPU's.")
        }.get(self.gpu_manufacturer, lambda: Handler.exception("Unsupported platform"))
        return fun()

    def gpu_memory_total(self):
        """
            Returns your GPU's total available memory
        """
        fun = {
            'nvidia': nvidia.gpu_memory_total,
            'amd': lambda: Handler.exception("Error: Currently os.py does not support AMD GPU's.")
        }.get(self.gpu_manufacturer, lambda: Handler.exception("Unsupported platform"))
        return fun()

    def gpu_memory_free(self):
        """
            Returns your GPU's free memory
        """
        fun = {
            'nvidia': nvidia.gpu_memory_free,
            'amd': lambda: Handler.exception("Error: Currently os.py does not support AMD GPU's.")
        }.get(self.gpu_manufacturer, lambda: Handler.exception("Unsupported platform"))
        return fun()

    def gpu_memory_used(self):
        """
            Returns your GPU's used memory
        """
        fun = {
            'nvidia': nvidia.gpu_memory_used,
            'amd': lambda: Handler.exception("Error: Currently os.py does not support AMD GPU's.")
        }.get(self.gpu_manufacturer, lambda: Handler.exception("Unsupported platform"))
        return fun()

    def gpu_display_mode(self):
        """
            Returns your GPU's display mode
        """
        fun = {
            'nvidia': nvidia.gpu_display_mode,
            'amd': lambda: Handler.exception("Error: Currently os.py does not support AMD GPU's.")
        }.get(self.gpu_manufacturer, lambda: Handler.exception("Unsupported platform"))
        return fun()

    def gpu_display_active(self):
        """
            Returns your GPU's active display
        """
        fun = {
            'nvidia': nvidia.gpu_display_active,
            'amd': lambda: Handler.exception("Error: Currently os.py does not support AMD GPU's.")
        }.get(self.gpu_manufacturer, lambda: Handler.exception("Unsupported platform"))
        return fun()


class ram:
    @staticmethod
    def ram_capacity():
        """
            Detects your entire RAM memory capacity
        """
        fun = {
            'windows': winram.win32_ram_capacity,
            'linux': lambda: Handler.exception("Error: Currently still working on linux ram functions.")
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def ram_form_factor():
        """
            Detects your RAM's form factor
        """
        fun = {
            'windows': winram.win32_ram_form_factor,
            'linux': lambda: Handler.exception("Error: Currently still working on linux ram functions.")
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def ram_memory_type():
        """
            Detects your RAM's memory type
        """
        fun = {
            'windows': winram.win32_ram_memory_type,
            'linux': lambda: Handler.exception("Error: Currently still working on linux ram functions.")
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def ram_manufacturer():
        """
            Detects your RAM's manufacturer
        """
        fun = {
            'windows': winram.win32_ram_manufacturer,
            'linux': lambda: Handler.exception("Error: Currently still working on linux ram functions.")
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def ram_clockspeed():
        """
            Detects your RAM'S clockspeed
        """
        fun = {
            'windows': winram.win32_ram_clockspeed,
            'linux': lambda: Handler.exception("Error: Currently still working on linux ram functions.")
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def ram_serial_number():
        """
            Detects your RAM's serial number
        """
        fun = {
            'windows': winram.win32_ram_serial_number,
            'linux': lambda: Handler.exception("Error: Currently still working on linux ram functions.")
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()


class storage:
    @staticmethod
    def _default_letter():
        return {
            'windows': 'C:\\',
            'linux': '/'
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))

    @staticmethod
    def drive_list():
        """
            Returns all drives on your device
        """
        fun = {
            'windows': _storage.drive_list,
            'linux': _storage.drive_list
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    def get_total_space(self, drive_letter=None):
        """
            Returns total space of your selected drive

            Accepts 1 param: drive letter (optional)
            Defaults:
                Windows : 'C:\\'
                Linux: '/'

            Basically, the parameter defines the drive the data will be from.
        """
        if drive_letter is None:
            drive_letter = self._default_letter()

        fun = {
            'windows': _storage.get_total_space,
            'linux': _storage.get_total_space
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun(drive_letter)

    def get_used_space(self, drive_letter=None):
        """
            Returns used space of your selected drive

            Accepts 1 param: drive letter (optional)
            Defaults:
                Windows : 'C:\\'
                Linux: '/'

            Basically, the parameter defines the drive the data will be from.
        """
        if drive_letter is None:
            drive_letter = self._default_letter()

        fun = {
            'windows': _storage.get_used_space,
            'linux': _storage.get_used_space
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun(drive_letter)

    def get_free_space(self, drive_letter=None):
        """
            Returns free space of your selected drive

            Accepts 1 param: drive letter (optional)
            Defaults:
                Windows : 'C:\\'
                Linux: '/'

            Basically, the parameter defines the drive the data will be from.
        """
        if drive_letter is None:
            drive_letter = self._default_letter()

        fun = {
            'windows': _storage.get_free_space,
            'linux': _storage.get_free_space
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun(drive_letter)

    def get_used_space_percent(self, drive_letter=None):
        """
            Returns used space of your selected drive as percentage

            Accepts 1 param: drive letter (optional)
            Defaults:
                Windows : 'C:\\'
                Linux: '/'

            Basically, the parameter defines the drive the data will be from.
        """
        if drive_letter is None:
            drive_letter = self._default_letter()

        fun = {
            'windows': _storage.get_used_space_percent,
            'linux': _storage.get_used_space_percent
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun(drive_letter)


class motherboard:
    @staticmethod
    def model():
        """
           Returns your current motherboard model
        """
        fun = {
            'windows': wmb.motherboard_model,
            'linux': lmb.motherboard_model
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def manufacturer():
        """
           Returns your current motherboard manufacturer
        """
        fun = {
            'windows': wmb.motherboard_manufacturer,
            'linux': lmb.motherboard_manufacturer
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def serial_number():
        """
           Returns your current motherboard serial number
        """
        fun = {
            'windows': wmb.motherboard_serial_number,
            'linux': lmb.motherboard_serial_number
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def version():
        """
           Returns your current motherboard version
        """
        fun = {
            'windows': wmb.motherboard_version,
            'linux': lmb.motherboard_version
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def node():
        """
           Returns your current motherboard node
        """
        fun = {
            'windows': wmb.motherboard_node,
            'linux': lmb.motherboard_node
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()


class device:
    @staticmethod
    def lst_extern_drives():
        """
            Lists external drives connected to your device
        """
        fun = {
            'windows': wdev.get_usb_list,
            'linux': ldev.get_usb_list
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()


class sound:
    @staticmethod
    def get_sound_devices():
        """
            Lists all connected sound devices
        """
        fun = {
            'windows': wso.get_audio_devices,
            'linux': lso.get_audio_devices
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()


class battery:
    @staticmethod
    def battery_percentage():
        """
            Returns users internet download speed
        """
        fun = {
            'windows': _battery.battery_percentage,
            'linux': _battery.battery_percentage
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def is_plugged_in():
        """
            Returns if users device is plugged in
        """
        fun = {
            'windows': _battery.is_plugged_in,
            'linux': _battery.is_plugged_in
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def battery_time_left():
        """
            Returns users estimated remaining battery life
        """
        fun = {
            'windows': _battery.battery_time_left,
            'linux': _battery.battery_time_left
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()


class network:
    @staticmethod
    def get_ipv4():
        """
            Returns user IpV4 address
        """
        fun = {
            'windows': _inet.get_ipv4,
            'linux': _inet.get_ipv4
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def get_ipv6():
        """
            Returns user IpV6 address
        """
        fun = {
            'windows': _inet.get_ipv6,
            'linux': _inet.get_ipv6
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def get_subnet_mask():
        """
            Returns user subnet mask
        """
        fun = {
            'windows': _inet.get_subnet_mask,
            'linux': _inet.get_subnet_mask
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def get_default_gateway():
        """
            Returns user default gateway
        """
        fun = {
            'windows': _inet.get_default_gateway,
            'linux': _inet.get_default_gateway
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def is_connected():
        """
            Returns users internet connection state (connected/disconnected)
        """
        fun = {
            'windows': _inet.is_connected,
            'linux': _inet.is_connected
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def get_hostname():
        """
            Returns user host name
        """
        fun = {
            'windows': _inet.get_hostname,
            'linux': _inet.get_hostname
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def get_ping_time():
        """
            Returns user ping time
        """
        fun = {
            'windows': _inet.get_ping_time,
            'linux': _inet.get_ping_time
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def user_download_speed():
        """
            Returns users internet download speed
        """
        fun = {
            'windows': _inet.get_download_speed,
            'linux': _inet.get_download_speed
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def user_upload_speed():
        """
            Returns users internet upload speed
        """
        fun = {
            'windows': _inet.get_upload_speed,
            'linux': _inet.get_upload_speed
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()


class machine:
    @staticmethod
    def machine_name():
        """
            Detects machines names and returns it to the user
        """
        fun = {
            'windows': _machine.machine_name,
            'linux': _machine.machine_name
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()

    @staticmethod
    def boot_type():
        """
            Detects your operating system's boot method (BIOS/UEFI)
        """
        fun = {
            'windows': wmach.boot_type,
            'linux': lmach.boot_type
        }.get(platform.system().lower(), lambda: Handler.exception("Unsupported platform"))
        return fun()
