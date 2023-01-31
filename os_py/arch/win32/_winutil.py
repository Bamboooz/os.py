import os
import subprocess
import winreg


class DataSources:
    @staticmethod
    def wmic_available(command):
        try:
            run_and_get_stdout(command)
            return True
        except Exception:
            return False

    @staticmethod
    def regedit_available(winreg_key_name):
        return winreg_key_exists(winreg_key_name)


def run_and_get_stdout(command):
    output = subprocess.getoutput(command).strip()  # get the output from Windows cmd
    output = output.split("\n", 1)[1]  # remove first line which is the data name
    output = os.linesep.join([s for s in output.splitlines() if s])  # remove blank lines

    format_string = ''  # string that will contain the formatted output

    for line in output.splitlines():
        if len(output.split('\n')) == 1:
            format_string += line.strip()
        else:
            format_string += line.strip() + '\n'

    if len(output.split('\n')) == 1:
        return format_string.strip()
    else:
        return os.linesep.join([s.strip() for s in format_string.splitlines() if s])


def read_windows_registry_key(winreg_key_name):
    # set winreg field and key
    key_name = winreg_key_name[0]
    field_name = winreg_key_name[1]

    # read regedit key
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_name)
    value = winreg.QueryValueEx(key, field_name)[0]
    winreg.CloseKey(key)

    return value


def winreg_key_exists(winreg_key_name):
    # set winreg field and key
    key_name = winreg_key_name[0]
    field_name = winreg_key_name[1]

    if field_name != '':
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_name)
            value = winreg.QueryValueEx(key, field_name)[0]
            winreg.CloseKey(key)
            return True
        except FileNotFoundError:
            return False

    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        winreg.OpenKey(reg, key_name)
        winreg.CloseKey(reg)
        return True
    except FileNotFoundError:
        return False
