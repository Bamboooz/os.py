import distro

from collections import defaultdict
from scripts.err import Errors as err


def get_distro():
    linux_distribution = distro.id()

    func_os = defaultdict(lambda: err.print_err('Error: Unsupported linux distro.'),
                          ubuntu='Ubuntu',
                          debian='Debian',
                          rhel='RedHat Enterprise Linux',
                          centos='CentOS',
                          fedora='Fedora',
                          sles='SUSE Linux Enterprise Server',
                          opensuse='openSUSE',
                          amazon='Amazon Linux',
                          arch='Arch Linux',
                          cloudlinux='CloudLinux OS',
                          exherbo='Exherbo Linux',
                          gentoo='GenToo Linux',
                          ibm_powerkvm='IBM PowerKVM',
                          kvmibm='KVM for IBM z Systems',
                          linuxmint='Linux Mint',
                          mageia='Mageia',
                          mandriva='Mandriva Linux',
                          parallels='Parallels',
                          pidora='Pidora',
                          raspbian='Raspbian',
                          oracle='Oracle Linux (and Oracle Enterprise Linux)',
                          scientific='Scientific Linux',
                          slackware='Slackware',
                          xenserver='XenServer')
    return func_os[linux_distribution]


def linux_distro():
    return str(get_distro())
