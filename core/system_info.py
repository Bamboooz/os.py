import platform
import sys
import distro
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
