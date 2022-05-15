import subprocess
import sys
import psutil
from core.exception import *


def ram_total_memory():
    if sys.platform == 'win32' or 'linux':
        return str(psutil.virtual_memory().total / (1024 ** 3)) + ' GB'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def ram_manufacturer():
    if sys.platform == 'win32':
        manufacturer = subprocess.check_output('wmic memorychip get manufacturer').decode().split('\n')[1].strip()
        return manufacturer
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def ram_serial_number():
    if sys.platform == 'win32':
        serialnumber = subprocess.check_output('wmic memorychip get serialnumber').decode().split('\n')[1].strip()
        return serialnumber
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def ram_memory_type():
    if sys.platform == 'win32':
        memorytype = subprocess.check_output('wmic memorychip get memorytype').decode().split('\n')[1].strip()
        types = ['Unknown', 'Other', 'DRAM', 'Synchronous DRAM', 'Cache DRAM', 'EDO', 'EDRAM', 'VRAM',
                 'SRAM', 'RAM', 'ROM', 'Flash', 'EEPROM', 'FEPROM', 'EPROM', 'CDRAM', '3DRAM', 'SDRAM',
                 'SGRAM', 'RDRAM', 'DDR', 'DDR2', 'DDR2 FB-DIMM', 'DDR3', 'FBD2', 'DDR4']
        return str(types[int(memorytype)])
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def ram_form_factor():
    if sys.platform == 'win32':
        factor = subprocess.check_output('wmic memorychip get memorytype').decode().split('\n')[1].strip()
        factors = ['Unknown', 'Other', 'SIP', 'DIP', 'ZIP', 'SOJ', 'Proprietary', 'SIMM',
                   'DIMM', 'TSOP', 'PGA', 'RIMM', 'SODIMM', 'SRIMM', 'SMD', 'SSMP', 'QFP',
                   'TQFP', 'SOIC', 'LCC', 'PLCC', 'BGA', 'FPBGA', 'LGA', 'FB-DIMM']
        return str(factors[int(factor)])
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def ram_clockspeed():
    if sys.platform == 'win32':
        clockspeed = subprocess.check_output('wmic memorychip get speed').decode().split('\n')[1].strip()
        return str(clockspeed) + 'Hz'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return unsupported_exception()
    else:
        return unsupported_exception()


def ram_usage():
    if sys.platform == 'win32' or 'linux':
        return str(psutil.virtual_memory()[2]) + '%'
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()
