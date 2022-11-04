def unsupported_exception():
    return "\033[91mError: PySil library does not support your operating system.\033[0m"


def unsupported_func():
    return "\033[91mError: Currently function your trying to use is unavailable for your operating system.\033[0m"


def feature_not_implemented_yet():
    return "\033[91mError: Feature not implemented yet - should be available in next versions.\033[0m"


def no_linux_driver():
    return "\033[91mError: Your Linux system does not have driver required to get this parameter.\033[0m"


def not_linux():
    return "\033[91mError: To run this function your os must be Linux.\033[0m"


def distro_not_found():
    return "\033[91mError: Linux distribution not found or not supported by PySil library.\033[0m"


def unknown_exception():
    return "\033[91mError: Unknown error occurred.\033[0m"


def no_admin_perms():
    return "\033[91mError: To get this data you need to run your application as administrator.\033[0m"
