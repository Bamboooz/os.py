import subprocess
import sys
import psutil
from core.exception import *


def ram_total_memory():
    if sys.platform == 'win32':
        return str(round(psutil.virtual_memory().total / (1024 ** 3))) + 'GB'
    else:
        return unsupported_exception()


def ram_manufacturer():
    if sys.platform == 'win32':
        manufacturer = subprocess.check_output('wmic memorychip get manufacturer').decode().split('\n')[1].strip()
        return manufacturer
    else:
        return unsupported_exception()


def ram_serial_number():
    if sys.platform == 'win32':
        serialnumber = subprocess.check_output('wmic memorychip get serialnumber').decode().split('\n')[1].strip()
        return serialnumber
    else:
        return unsupported_exception()


def ram_memory_type():
    if sys.platform == 'win32':
        memorytype = subprocess.check_output('wmic memorychip get memorytype').decode().split('\n')[1].strip()
        types = ['Unknown', 'Other', 'DRAM', 'Synchronous DRAM', 'Cache DRAM', 'EDO', 'EDRAM', 'VRAM',
                 'SRAM', 'RAM', 'ROM', 'Flash', 'EEPROM', 'FEPROM', 'EPROM', 'CDRAM', '3DRAM', 'SDRAM',
                 'SGRAM', 'RDRAM', 'DDR', 'DDR2', 'DDR2 FB-DIMM', 'DDR3', 'FBD2', 'DDR4']
        return str(types[int(memorytype)])
    else:
        return unsupported_exception()


def ram_form_factor():
    if sys.platform == 'win32':
        factor = subprocess.check_output('wmic memorychip get memorytype').decode().split('\n')[1].strip()
        factors = ['Unknown', 'Other', 'SIP', 'DIP', 'ZIP', 'SOJ', 'Proprietary', 'SIMM',
                   'DIMM', 'TSOP', 'PGA', 'RIMM', 'SODIMM', 'SRIMM', 'SMD', 'SSMP', 'QFP',
                   'TQFP', 'SOIC', 'LCC', 'PLCC', 'BGA', 'FPBGA', 'LGA', 'FB-DIMM']
        return str(factors[int(factor)])
    else:
        return unsupported_exception()


def ram_clockspeed():
    if sys.platform == 'win32':
        clockspeed = subprocess.check_output('wmic memorychip get speed').decode().split('\n')[1].strip()
        return str(clockspeed) + 'Hz'
    else:
        return unsupported_exception()


def ram_usage():
    if sys.platform == 'win32':
        return str(psutil.virtual_memory()[2]) + '%'
    else:
        return unsupported_exception()
