import platform

from collections import defaultdict

from scripts.err import Errors
from os_py import _battery, _inet, _machine, _sys, _cpu

from os_py.arch.linux import ldistro

from os_py.arch.linux import machine as lmach
from os_py.arch.linux import device as ldev
from os_py.arch.linux import sound as lso
from os_py.arch.linux import motherboard as lmb
from os_py.arch.linux import temp as ltmp

from os_py.arch.windows import machine as wmach
from os_py.arch.windows import device as wdev
from os_py.arch.windows import sound as wso
from os_py.arch.windows import motherboard as wmb
from os_py.arch.windows import temp as wtmp


class system:  # access for system functions from library
    @staticmethod
    def os_name():
        """
            Returns operating system's name e.g. Windows, Linux etc.
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_sys.os_name(),
                              linux=_sys.os_name(),
                              linux2=_sys.os_name())
        return func_os[platform.system().lower()]

    @staticmethod
    def os_version():
        """
            Returns operating system's version e.g. Windows 10
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_sys.os_version(),
                              linux=_sys.os_version(),
                              linux2=_sys.os_version())
        return func_os[platform.system().lower()]

    @staticmethod
    def os_platform():
        """
            Returns a single string identifying the underlying platform
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_sys.os_platform(),
                              linux=_sys.os_platform(),
                              linux2=_sys.os_platform())
        return func_os[platform.system().lower()]

    @staticmethod
    def os_release():
        """
            Detects your operating system's release e.g. Windows 10 22H2
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_sys.os_release(),
                              linux=_sys.os_release(),
                              linux2=_sys.os_release())
        return func_os[platform.system().lower()]

    @staticmethod
    def os_architecture():
        """
            Detects operating systems architecture e.g. 32-bit or 64-bit
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_sys.os_architecture(),
                              linux=_sys.os_architecture(),
                              linux2=_sys.os_architecture())
        return func_os[platform.system().lower()]

    @staticmethod
    def linux_distro():
        """
            Detects specific distributions on Linux-based systems
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=Errors().no_support(),
                              linux=ldistro.linux_distro(),
                              linux2=ldistro.linux_distro())
        return func_os[platform.system().lower()]


class machine:
    @staticmethod
    def machine_name():
        """
            Detects machines names and returns it to the user
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_machine.machine_name(),
                              linux=_machine.machine_name(),
                              linux2=_machine.machine_name())
        return func_os[platform.system().lower()]

    @staticmethod
    def boot_type():
        """
            Detects your operating system's boot method (BIOS/UEFI)
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=wmach.boot_type(),
                              linux=lmach.boot_type(),
                              linux2=lmach.boot_type())
        return func_os[platform.system().lower()]


class device:
    @staticmethod
    def lst_extern_drives():
        """
            Lists external drives connected to your device
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=wdev.get_usb_list(),
                              linux=ldev.get_usb_list(),
                              linux2=ldev.get_usb_list())
        return func_os[platform.system().lower()]


class network:
    @staticmethod
    def get_ipv4():
        """
            Returns user IpV4 address
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_inet.get_ipv4(),
                              linux=_inet.get_ipv4(),
                              linux2=_inet.get_ipv4())
        return func_os[platform.system().lower()]

    @staticmethod
    def get_ipv6():
        """
            Returns user IpV6 address
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_inet.get_ipv6(),
                              linux=_inet.get_ipv6(),
                              linux2=_inet.get_ipv6())
        return func_os[platform.system().lower()]

    @staticmethod
    def get_subnet_mask():
        """
            Returns user subnet mask
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_inet.get_subnet_mask(),
                              linux=_inet.get_subnet_mask(),
                              linux2=_inet.get_subnet_mask())
        return func_os[platform.system().lower()]

    @staticmethod
    def get_default_gateway():
        """
            Returns user default gateway
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_inet.get_default_gateway(),
                              linux=_inet.get_default_gateway(),
                              linux2=_inet.get_default_gateway())
        return func_os[platform.system().lower()]

    @staticmethod
    def is_connected():
        """
            Returns users internet connection state (connected/disconnected)
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_inet.is_connected(),
                              linux=_inet.is_connected(),
                              linux2=_inet.is_connected())
        return func_os[platform.system().lower()]

    @staticmethod
    def get_hostname():
        """
            Returns user host name
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_inet.get_hostname(),
                              linux=_inet.get_hostname(),
                              linux2=_inet.get_hostname())
        return func_os[platform.system().lower()]

    @staticmethod
    def get_ping_time():
        """
            Returns user ping time
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_inet.get_ping_time(),
                              linux=_inet.get_ping_time(),
                              linux2=_inet.get_ping_time())
        return func_os[platform.system().lower()]

    @staticmethod
    def user_download_speed():
        """
            Returns users internet download speed
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_inet.get_download_speed(),
                              linux=_inet.get_download_speed(),
                              linux2=_inet.get_download_speed())
        return func_os[platform.system().lower()]

    @staticmethod
    def user_upload_speed():
        """
            Returns users internet upload speed
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_inet.get_upload_speed(),
                              linux=_inet.get_upload_speed(),
                              linux2=_inet.get_upload_speed())
        return func_os[platform.system().lower()]


class battery:
    @staticmethod
    def battery_percentage():
        """
            Returns users internet download speed
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_battery.battery_percentage(),
                              linux=_battery.battery_percentage(),
                              linux2=_battery.battery_percentage())
        return func_os[platform.system().lower()]

    @staticmethod
    def is_plugged_in():
        """
            Returns if users device is plugged in
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_battery.is_plugged_in(),
                              linux=_battery.is_plugged_in(),
                              linux2=_battery.is_plugged_in())
        return func_os[platform.system().lower()]

    @staticmethod
    def battery_time_left():
        """
            Returns users estimated remaining battery life
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_battery.battery_time_left(),
                              linux=_battery.battery_time_left(),
                              linux2=_battery.battery_time_left())
        return func_os[platform.system().lower()]


class sound:
    @staticmethod
    def get_sound_devices():
        """
            Lists all connected sound devices
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=wso.get_audio_devices(),
                              linux=lso.get_audio_devices(),
                              linux2=lso.get_audio_devices())
        return func_os[platform.system().lower()]


class motherboard:
    @staticmethod
    def model():
        """
           Returns your current motherboard model
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=wmb.motherboard_model(),
                              linux=lmb.motherboard_model(),
                              linux2=lmb.motherboard_model())
        return func_os[platform.system().lower()]

    @staticmethod
    def manufacturer():
        """
           Returns your current motherboard manufacturer
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=wmb.motherboard_manufacturer(),
                              linux=lmb.motherboard_manufacturer(),
                              linux2=lmb.motherboard_manufacturer())
        return func_os[platform.system().lower()]

    @staticmethod
    def serial_number():
        """
           Returns your current motherboard serial number
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=wmb.motherboard_serial_number(),
                              linux=lmb.motherboard_serial_number(),
                              linux2=lmb.motherboard_serial_number())
        return func_os[platform.system().lower()]

    @staticmethod
    def version():
        """
           Returns your current motherboard version
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=wmb.motherboard_version(),
                              linux=lmb.motherboard_version(),
                              linux2=lmb.motherboard_version())
        return func_os[platform.system().lower()]

    @staticmethod
    def node():
        """
           Returns your current motherboard node
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=wmb.motherboard_node(),
                              linux=lmb.motherboard_node(),
                              linux2=lmb.motherboard_node())
        return func_os[platform.system().lower()]


class cpu:
    @staticmethod
    def cpu_model():
        """
             Returns your current processor model
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_cpu.cpu_model(),
                              linux=_cpu.cpu_model(),
                              linux2=_cpu.cpu_model())
        return func_os[platform.system().lower()]

    @staticmethod
    def cpu_physical_cores():
        """
            Returns number of physical cores that your cpu possesses
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_cpu.cpu_physical_cores(),
                              linux=_cpu.cpu_physical_cores(),
                              linux2=_cpu.cpu_physical_cores())
        return func_os[platform.system().lower()]

    @staticmethod
    def cpu_logical_cores():
        """
            Returns number of logical cores that your cpu possesses
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_cpu.cpu_logical_cores(),
                              linux=_cpu.cpu_logical_cores(),
                              linux2=_cpu.cpu_logical_cores())
        return func_os[platform.system().lower()]

    @staticmethod
    def cpu_total_cores():
        """
            Returns number of total cores that your cpu possesses
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_cpu.cpu_total_cores(),
                              linux=_cpu.cpu_total_cores(),
                              linux2=_cpu.cpu_total_cores())
        return func_os[platform.system().lower()]

    @staticmethod
    def cpu_clockspeed():
        """
            Returns your cpu's default clockspeed
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_cpu.cpu_clockspeed(),
                              linux=_cpu.cpu_clockspeed(),
                              linux2=_cpu.cpu_clockspeed())
        return func_os[platform.system().lower()]

    @staticmethod
    def cpu_architecture():
        """
            Returns your current cpu architecture
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_cpu.cpu_architecture(),
                              linux=_cpu.cpu_architecture(),
                              linux2=_cpu.cpu_clockspeed())
        return func_os[platform.system().lower()]

    @staticmethod
    def cpu_usage():
        """
            Returns your current processor usage
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_cpu.cpu_usage(),
                              linux=_cpu.cpu_usage(),
                              linux2=_cpu.cpu_usage())
        return func_os[platform.system().lower()]

    @staticmethod
    def cpu_vendor_id():
        """
            Returns your current cpu vendor id
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=_cpu.cpu_vendor_id(),
                              linux=_cpu.cpu_vendor_id(),
                              linux2=_cpu.cpu_vendor_id())
        return func_os[platform.system().lower()]

    @staticmethod
    def cpu_temperature(unit='C'):
        """
            Returns you cpu's current temperature

            Accepts 1 param, unit ['C', 'F', 'K'] (doesn't have to be uppercase)
            Specifies unit that the cpu temperature will be returned in.
            Optional parameter, default = 'C'
        """
        func_os = defaultdict(lambda: Errors().unsupported_os(),
                              windows=wtmp.cpu_temperature(unit),
                              linux=ltmp.cpu_temperature(unit),
                              linux2=ltmp.cpu_temperature(unit))
        return func_os[platform.system().lower()]
