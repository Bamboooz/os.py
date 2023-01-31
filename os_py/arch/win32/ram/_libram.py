import os_py.arch.win32._winutil as _winutil


class WMI_MEMORYCHIP:
    WIN32_WMI_CAPACITY = "wmic memorychip get capacity"
    WIN32_WMI_FORM_FACTOR = "wmic memorychip get formfactor"
    WIN32_WMI_MANUFACTURER = "wmic memorychip get manufacturer"
    WIN32_WMI_MEMORY_TYPE = "wmic memorychip get memorytype"
    WIN32_WMI_MODEL = "wmic memorychip get model"
    WIN32_WMI_CLOCKSPEED = "wmic memorychip get speed"
    WIN32_WMI_SERIAL_NUMBER = "wmic memorychip get serialnumber"


def win32_ram_capacity(method='wmic'):
    def win32_wmic_capacity():
        total_capacity = 0

        for line in _winutil.run_and_get_stdout(WMI_MEMORYCHIP.WIN32_WMI_CAPACITY).splitlines():
            total_capacity += int(line.strip())

        return str(round(total_capacity / 1073741824)) + 'GB'

    if method == 'wmic':
        return win32_wmic_capacity()


def win32_ram_form_factor(method='wmic'):
    def win32_wmic_form_factor():
        form_factor = _winutil.run_and_get_stdout(WMI_MEMORYCHIP.WIN32_WMI_FORM_FACTOR).splitlines()[0]
        factors = ['Unknown', 'Other', 'SIP', 'DIP', 'ZIP', 'SOJ', 'Proprietary', 'SIMM',
                   'DIMM', 'TSOP', 'PGA', 'RIMM', 'SODIMM', 'SRIMM', 'SMD', 'SSMP', 'QFP',
                   'TQFP', 'SOIC', 'LCC', 'PLCC', 'BGA', 'FPBGA', 'LGA', 'FB-DIMM']
        return str(factors[int(form_factor)])

    if method == 'wmic':
        return win32_wmic_form_factor()


def win32_ram_memory_type(method='wmic'):
    def win32_wmic_memory_type():
        memory_type = _winutil.run_and_get_stdout(WMI_MEMORYCHIP.WIN32_WMI_MEMORY_TYPE).splitlines()[0]
        types = ['Unknown', 'Other', 'DRAM', 'Synchronous DRAM', 'Cache DRAM', 'EDO', 'EDRAM', 'VRAM',
                 'SRAM', 'RAM', 'ROM', 'Flash', 'EEPROM', 'FEPROM', 'EPROM', 'CDRAM', '3DRAM', 'SDRAM',
                 'SGRAM', 'RDRAM', 'DDR', 'DDR2', 'DDR2 FB-DIMM', 'DDR3', 'FBD2', 'DDR4']
        return str(types[int(memory_type)])

    if method == 'wmic':
        return win32_wmic_memory_type()


def win32_ram_manufacturer(method='wmic'):
    def win32_wmic_manufacturer():
        return _winutil.run_and_get_stdout(WMI_MEMORYCHIP.WIN32_WMI_MANUFACTURER).splitlines()[0]

    if method == 'wmic':
        return win32_wmic_manufacturer()


def win32_ram_clockspeed(method='wmic'):
    def win32_wmic_clockspeed():
        return _winutil.run_and_get_stdout(WMI_MEMORYCHIP.WIN32_WMI_CLOCKSPEED).splitlines()[0]

    if method == 'wmic':
        return win32_wmic_clockspeed() + 'Hz'


def win32_ram_serial_number(method='wmic'):
    def win32_wmic_serial_number():
        return _winutil.run_and_get_stdout(WMI_MEMORYCHIP.WIN32_WMI_SERIAL_NUMBER).splitlines()[0]

    if method == 'wmic':
        return win32_wmic_serial_number()
