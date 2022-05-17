import os
import platform
import sys
import time
import psutil
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
    else:
        return unsupported_exception()


def os_platform():
    if sys.platform == 'win32':
        return platform.platform()
    else:
        return unsupported_exception()


def os_release():
    if sys.platform == 'win32':
        return platform.release()
    else:
        return unsupported_exception()


def os_architecture():
    if sys.platform == 'win32':
        return platform.machine()
    else:
        return unsupported_exception()


def process_list():
    if sys.platform == 'win32':
        plist = os.popen('tasklist').read()
        return plist
    else:
        return unsupported_exception()


def os_antivirus():
    if sys.platform == 'win32':
        avs_info = windows_tools.antivirus.get_installed_antivirus_software()
        av_data = [str(i).replace("'name': ", '').replace("'", '').split(', ') for i in avs_info]
        avs = list(
            str([str(x).split(', ', 1)[0] for x in av_data]).replace('[', '').replace('"', '').replace("'", '').replace(
                "{", '').replace("]", '').split(', '))
        return list(set(avs))
    else:
        return unsupported_exception()


def os_uptime():
    if sys.platform == 'win32':
        return str(round((time.time() - psutil.boot_time()) / 60 / 60)) + 'h'
    else:
        return unsupported_exception()
