import platform, psutil, time, sys


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


def os_uptime():
    if ((time.time() - psutil.boot_time()) / 60 / 60) > 1:
        return str((time.time() - psutil.boot_time()) / 60 / 60) + 'h'
    else:
        return str(round((time.time() - psutil.boot_time()) / 60)) + 'min'
