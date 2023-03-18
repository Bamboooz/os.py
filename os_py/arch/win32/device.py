import os_py.arch.win32._winutil as _winutils


def get_usb_list():
    return _winutils.run_and_get_stdout("wmic logicaldisk where drivetype=2 get DeviceID, VolumeName, Description")
