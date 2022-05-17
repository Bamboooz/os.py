import ipaddress
import socket
import netifaces
import sys
from core.exception import *


def get_ipv4():
    if sys.platform == 'win32':
        hostname = socket.gethostname()
        ipv4 = socket.gethostbyname(hostname)
        return ipv4
    else:
        return unsupported_exception()


def get_ipv6():
    if sys.platform == 'win32':
        alladdr = socket.getaddrinfo(socket.gethostname(), 0)
        ip6 = filter(
            lambda x: x[0] == socket.AF_INET6,  # means its ip6
            alladdr
        )
        return list(ip6)[0][4][0]
    else:
        return unsupported_exception()


def get_subnet_mask():
    if sys.platform == 'win32':
        ip_addr = socket.gethostbyname(socket.gethostname())
        netmask = ipaddress.IPv4Network(ip_addr).netmask
        return netmask
    else:
        return unsupported_exception()


def get_default_gateway():
    if sys.platform == 'win32':
        gateways = netifaces.gateways()
        defaults = gateways.get("default")
        if not defaults:
            return

        def default_ip(family):
            gw_info = defaults.get(family)
            if not gw_info:
                return
            addresses = netifaces.ifaddresses(gw_info[1]).get(family)
            if addresses:
                return addresses[0]["addr"]

        return default_ip(netifaces.AF_INET) or default_ip(netifaces.AF_INET6)
    else:
        return unsupported_exception()


def is_connected():
    if sys.platform == 'win32':
        try:
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            return True
        except socket.error:
            return False
    else:
        return unsupported_exception()


def get_hostname():
    if sys.platform == 'win32':
        return socket.gethostname()
    else:
        return unsupported_exception()
