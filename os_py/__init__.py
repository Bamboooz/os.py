import sys

from scripts.err import Errors
from os_py import _battery, _inet, _machine, _sys

from os_py.arch.linux import ldistro

from os_py.arch.linux import machine as lmach
from os_py.arch.linux import device as ldev

from os_py.arch.windows import machine as wmach
from os_py.arch.windows import device as wdev


class system:  # access for system functions from library
    @staticmethod
    def os_name():
        """
            Returns operating system's name e.g. Windows, Linux etc.
        """
        return {
            'windows' or 'linux' or 'linux2': _sys.os_name()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def os_version():
        """
            Returns operating system's version e.g. Windows 10
        """
        return {
            'windows' or 'linux' or 'linux2': _sys.os_version()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def os_platform():
        """
            Returns a single string identifying the underlying platform
        """
        return {
            'windows' or 'linux' or 'linux2': _sys.os_platform()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def os_release():
        """
            Detects your operating system's release e.g. Windows 10 22H2
        """
        return {
            'windows' or 'linux' or 'linux2': _sys.os_release()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def os_architecture():
        """
            Detects operating systems architecture e.g. 32-bit or 64-bit
        """
        return {
            'windows' or 'linux' or 'linux2': _sys.os_architecture()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def linux_distro():
        """
            Detects specific distributions on Linux-based systems
        """
        return {
            'linux' or 'linux2': ldistro.linux_distro(),
            'windows': Errors().no_support()
        }.get(sys.platform.lower(), Errors().unsupported_os())


class machine:
    @staticmethod
    def machine_name():
        """
            Detects machines names and returns it to the user
        """
        return {
            'windows' or 'linux' or 'linux2': _machine.machine_name()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def sys_start_method():
        """
            Detects your operating system's boot method (BIOS/UEFI)
        """
        return {
            'windows': wmach.bios_type(),
            'linux' or 'linux2': lmach.bios_type()
        }.get(sys.platform.lower(), Errors().unsupported_os())


class device:
    @staticmethod
    def lst_extern_drives():
        """
            Lists external drives connected to your device
        """
        return {
            'windows': wdev.get_usb_list(),
            'linux' or 'linux2': ldev.get_usb_list()
        }.get(sys.platform.lower(), Errors().unsupported_os())


class network:
    @staticmethod
    def get_ipv4():
        """
            Returns user IpV4 address
        """
        return {
            'windows' or 'linux' or 'linux2': _inet.get_ipv4()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def get_ipv6():
        """
            Returns user IpV6 address
        """
        return {
            'windows' or 'linux' or 'linux2': _inet.get_ipv6()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def get_subnet_mask():
        """
            Returns user subnet mask
        """
        return {
            'windows' or 'linux' or 'linux2': _inet.get_subnet_mask()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def get_default_gateway():
        """
            Returns user default gateway
        """
        return {
            'windows' or 'linux' or 'linux2': _inet.get_default_gateway()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def is_connected():
        """
            Returns users internet connection state (connected/disconnected)
        """
        return {
            'windows' or 'linux' or 'linux2': _inet.is_connected()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def get_hostname():
        """
            Returns user host name
        """
        return {
            'windows' or 'linux' or 'linux2': _inet.get_hostname()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def get_ping_time():
        """
            Returns user ping time
        """
        return {
            'windows' or 'linux' or 'linux2': _inet.get_ping_time()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def user_download_speed():
        """
            Returns users internet download speed
        """
        return {
            'windows' or 'linux' or 'linux2': _inet.get_download_speed()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def user_upload_speed():
        """
            Returns users internet upload speed
        """
        return {
            'windows' or 'linux' or 'linux2': _inet.get_upload_speed()
        }.get(sys.platform.lower(), Errors().unsupported_os())


class battery:
    @staticmethod
    def battery_percentage():
        """
            Returns users internet download speed
        """
        return {
            'windows' or 'linux' or 'linux2': _battery.battery_percentage()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def is_plugged_in():
        """
            Returns if users device is plugged in
        """
        return {
            'windows' or 'linux' or 'linux2': _battery.is_plugged_in()
        }.get(sys.platform.lower(), Errors().unsupported_os())

    @staticmethod
    def battery_time_left():
        """
            Returns users estimated remaining battery life
        """
        return {
            'windows' or 'linux' or 'linux2': _battery.battery_time_left()
        }.get(sys.platform.lower(), Errors().unsupported_os())
