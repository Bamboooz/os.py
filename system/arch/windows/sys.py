import ctypes


def is_admin():
    # Return if current user is an administrator.
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
