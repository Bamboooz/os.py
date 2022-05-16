import os
import platform
import sys
import distro
import windows_tools.antivirus
from core.exception import *


def os_name():
    if sys.platform.startswith("linux"):
        return 'Linux'
    elif sys.platform == "darwin":
        return 'MacOS'
    elif sys.platform == "win32":
        return 'Windows'
    else:
        return unsupported_exception()


def os_version():
    if sys.platform == 'win32':
        return platform.version().split('.')[2]
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return distro.id() + ' ' + platform.release()
    else:
        return unsupported_exception()


def linux_distro():
    if sys.platform == 'linux':
        return distro.id()
    else:
        return not_linux()


def os_platform():
    if sys.platform == 'win32' or 'linux':
        return platform.platform()
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def os_release():
    if sys.platform == 'win32' or 'linux':
        return platform.release()
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def os_architecture():
    if sys.platform == 'win32' or 'linux':
        return platform.machine()
    elif sys.platform == 'darwin':
        return unsupported_exception()
    else:
        return unsupported_exception()


def process_list():
    plist = os.popen('tasklist').read()
    return plist


def os_antivirus():
    avs_info = windows_tools.antivirus.get_installed_antivirus_software()
    av_data = [str(i).replace("'name': ", '').replace("'", '').split(', ') for i in avs_info]
    avs = list(str([str(x).split(', ', 1)[0] for x in av_data]).replace('[', '').replace('"', '').replace("'", '').replace("{", '').replace("]", '').split(', '))
    return list(set(avs))
