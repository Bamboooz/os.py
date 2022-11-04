import os
import platform
import sys
import time
import distro
import subprocess
import psutil
import windows_tools.antivirus
from core.exception import *


def get_distro():
    linux_distribution = distro.id()
    return {
        'ubuntu': 'Ubuntu',
        'debian': 'Debian',
        'rhel': 'RedHat Enterprise Linux',
        'centos': 'CentOS',
        'fedora': 'Fedora',
        'sles': 'SUSE Linux Enterprise Server',
        'opensuse': 'openSUSE',
        'amazon': 'Amazon Linux',
        'arch': 'Arch Linux',
        'cloudlinux': 'CloudLinux OS',
        'exherbo': 'Exherbo Linux',
        'gentoo': 'GenToo Linux',
        'ibm_powerkvm': 'IBM PowerKVM',
        'kvmibm': 'KVM for IBM z Systems',
        'linuxmint': 'Linux Mint',
        'mageia': 'Mageia',
        'mandriva': 'Mandriva Linux',
        'parallels': 'Parallels',
        'pidora': 'Pidora',
        'raspbian': 'Raspbian',
        'oracle': 'Oracle Linux (and Oracle Enterprise Linux)',
        'scientific': 'Scientific Linux',
        'slackware': 'Slackware',
        'xenserver': 'XenServer',
        'openbsd': 'OpenBSD',
        'netbsd': 'NetBSD',
        'freebsd': 'FreeBSD',
    }.get(linux_distribution, distro_not_found)


def os_name():
    if sys.platform == 'win32':
        return 'Windows'
    elif sys.platform == "darwin":
        return 'MacOS'
    elif sys.platform == 'linux':
        return 'Linux'
    else:
        print(unsupported_exception())


def os_version():
    if sys.platform == 'win32':
        return platform.version().split('.')[2]
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        return str(get_distro()) + ' ' + platform.release()
    else:
        print(unsupported_exception())


def linux_distro():
    if sys.platform == 'linux':
        return str(get_distro())
    else:
        print(not_linux())


def os_platform():
    if sys.platform == 'win32' or 'linux':
        return platform.platform()
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def os_release():
    if sys.platform == 'win32' or 'linux':
        return platform.release()
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def os_architecture():
    if sys.platform == 'win32' or 'linux':
        return platform.machine()
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def process_list():
    if sys.platform == 'win32':
        plist = os.popen('tasklist').read()
        return plist
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        pl = str(subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE).communicate()[0]).split(r'\n')
        a = ''
        for i in pl:
            a += '\n' + str(i)
        return a
    else:
        print(unsupported_exception())


def os_uptime():
    if sys.platform == 'win32' or 'linux':
        if ((time.time() - psutil.boot_time()) / 60 / 60) > 1:
            return str((time.time() - psutil.boot_time()) / 60 / 60) + 'h'
        else:
            return str(round((time.time() - psutil.boot_time()) / 60)) + 'min'
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def os_antivirus():
    if sys.platform == 'win32':
        avs_info = windows_tools.antivirus.get_installed_antivirus_software()
        av_data = [str(i).replace("'name': ", '').replace("'", '').split(', ') for i in avs_info]
        avs = list(
            str([str(x).split(', ', 1)[0] for x in av_data]).replace('[', '').replace('"', '').replace("'", '').replace(
                "{", '').replace("]", '').split(', '))
        return list(set(avs))
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        print(feature_not_implemented_yet())
    else:
        print(unsupported_exception())
