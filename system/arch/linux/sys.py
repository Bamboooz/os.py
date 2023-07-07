import os


def is_admin():
    # Return if current user is an administrator.
    return os.geteuid() == 0
