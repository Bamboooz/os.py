import platform
import sys


def os_name():
    return sys.platform


def os_version():
    return platform.version().split('.')[2]


def os_platform():
    return platform.platform()


def os_release():
    return platform.release()


def os_architecture():
    return platform.machine()
