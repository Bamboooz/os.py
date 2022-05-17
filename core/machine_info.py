import platform
import re
import sys
from core.exception import *


def machine_name():
    if sys.platform == 'win32':
        return platform.node()
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
    else:
        return unsupported_exception()
