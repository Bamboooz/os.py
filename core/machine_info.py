import platform
import re
import sys
from core.exception import *


def machine_name():
    if sys.platform == 'win32' or 'linux':
        return platform.node()
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def bios_type():
    if sys.platform == 'win32':
        with open(r'C:\Windows\Panther\setupact.log') as f:
            pattern = re.compile(r'Detected boot environment: (\w+)')
            for line in f:
                match = pattern.search(line)
                if match:
                    boot_type = match.group(1).upper()
                    if boot_type == 'EFI':
                        return 'UEFI'
                    else:
                        return 'BIOS'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        try:
            open("/sys/firmware/efi")
            return 'UEFI'
        except IOError:
            return 'BIOS'
    else:
        return unsupported_exception()
