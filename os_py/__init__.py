import sys

from scripts.err import Errors as err

import os_py.arch.windows as win
import os_py.arch.linux as linux


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
    def test():
        return {
            'windows': "win.sys.os_name()",
            'linux' or 'linux2': "linux.sys.os_name()"
        }.get(sys.platform.lower())


class cpu:
    def __init__(self):
        self.sys = _set_sys.check_platform_compatibility()
