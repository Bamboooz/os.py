import platform


def os_name():
    return platform.system()


def os_version():
    return platform.version()


def os_platform():
    return platform.platform()


def os_release():
    return platform.release()


def os_architecture():
    return platform.machine()
