import subprocess


def is_lscpu_available():
    try:
        subprocess.getoutput('lscpu')
        return True
    except Exception:
        return False


def is_procinfo_available():
    try:
        subprocess.getoutput('cat /proc/cpuinfo')
        return True
    except Exception:
        return False
