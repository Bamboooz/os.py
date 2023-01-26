import sys

from scripts.err import Errors as err

import pysil.arch.windows as win
import pysil.arch.linux as linux


class _set_sys:
    @staticmethod
    def check_platform_compatibility():
        # handle unsupported operating systems
        supported_os = ['linux', 'linux2', 'windows']
        if sys.platform.lower() not in supported_os:
            err().unsupported_os()
        else:
            return sys.platform.lower()


class system:
    def __init__(self):
        self.sys = _set_sys.check_platform_compatibility()

    @staticmethod
    def os_name():
        return {
            'windows': win.sys.os_name(),
            'linux' or 'linux2': linux.sys.os_name()
        }.get(sys.platform.lower())

    @staticmethod
    def linux_distro():
        return {
            'windows': err().no_support(),
            'linux' or 'linux2': linux.sys.linux_distro()
        }.get(sys.platform.lower())

    @staticmethod
    def os_version():
        return {
            'windows': win.sys.os_version(),
            'linux' or 'linux2': linux.sys.os_version()
        }.get(sys.platform.lower())

    @staticmethod
    def os_platform():
        return {
            'windows': win.sys.os_platform(),
            'linux' or 'linux2': linux.sys.os_platform()
        }.get(sys.platform.lower())

    @staticmethod
    def os_release():
        return {
            'windows': win.sys.os_release(),
            'linux' or 'linux2': linux.sys.os_release()
        }.get(sys.platform.lower())

    @staticmethod
    def os_architecture():
        return {
            'windows': win.sys.os_architecture(),
            'linux' or 'linux2': linux.sys.os_architecture()
        }.get(sys.platform.lower())

    @staticmethod
    def process_list():
        return {
            'windows': win.sys.process_list(),
            'linux' or 'linux2': linux.sys.process_list()
        }.get(sys.platform.lower())

    @staticmethod
    def os_uptime():
        return {
            'windows': win.sys.os_uptime(),
            'linux' or 'linux2': linux.sys.os_uptime()
        }.get(sys.platform.lower())


class cpu:
    def __init__(self):
        self.sys = _set_sys.check_platform_compatibility()

    @staticmethod
    def cpu_model():
        return {
            'windows': win.cpu.cpu_model(),
            'linux' or 'linux2': linux.cpu.cpu_model()
        }.get(sys.platform.lower())

    @staticmethod
    def cpu_physical_cores():
        return {
            'windows': win.cpu.cpu_physical_cores(),
            'linux' or 'linux2': linux.cpu.cpu_physical_cores()
        }.get(sys.platform.lower())

    @staticmethod
    def cpu_logical_cores():
        return {
            'windows': win.cpu.cpu_logical_cores(),
            'linux' or 'linux2': linux.cpu.cpu_logical_cores()
        }.get(sys.platform.lower())

    @staticmethod
    def cpu_total_cores():
        return {
            'windows': win.cpu.cpu_total_cores(),
            'linux' or 'linux2': linux.cpu.cpu_total_cores()
        }.get(sys.platform.lower())

    @staticmethod
    def cpu_clockspeed():
        return {
            'windows': win.cpu.cpu_clockspeed(),
            'linux' or 'linux2': linux.cpu.cpu_clockspeed()
        }.get(sys.platform.lower())

    @staticmethod
    def cpu_architecture():
        return {
            'windows': win.cpu.cpu_architecture(),
            'linux' or 'linux2': linux.cpu.cpu_architecture()
        }.get(sys.platform.lower())

    @staticmethod
    def cpu_usage():
        return {
            'windows': win.cpu.cpu_usage(),
            'linux' or 'linux2': linux.cpu.cpu_usage()
        }.get(sys.platform.lower())

    @staticmethod
    def cpu_temperature(unit='C'):
        return {
            'windows': win.cpu.cpu_temperature(unit),
            'linux' or 'linux2': linux.cpu.cpu_temperature(unit)
        }.get(sys.platform.lower())

    @staticmethod
    def cpu_vendor_id():
        return {
            'windows': win.cpu.cpu_vendor_id(),
            'linux' or 'linux2': linux.cpu.cpu_vendor_id()
        }.get(sys.platform.lower())
