import os
import platform
import sys
import distro
import subprocess
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
    if sys.platform == 'win32':
        plist = os.popen('tasklist').read()
        return plist
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        pl = str(subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE).communicate()[0]).split(r'\n')
        a = ''
        for i in pl:
            a = a + '\n' + str(i)
        return a
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
    elif sys.platform == 'darwin':
        return unsupported_exception()
    elif sys.platform == 'linux':
        return feature_not_implemented_yet()
    else:
        return unsupported_exception()

