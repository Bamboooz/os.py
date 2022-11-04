import ipaddress
import socket
import netifaces
import sys
import speedtest
from core.exception import *


def get_ipv4():
    if sys.platform == 'win32' or 'linux':
        hostname = socket.gethostname()
        ipv4 = socket.gethostbyname(hostname)
        return ipv4
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def get_ipv6():
    if sys.platform == 'win32' or 'linux':
        alladdr = socket.getaddrinfo(socket.gethostname(), 0)
        ip6 = filter(
            lambda x: x[0] == socket.AF_INET6,  # means its ip6
            alladdr
        )
        return list(ip6)[0][4][0]
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def get_subnet_mask():
    if sys.platform == 'win32' or 'linux':
        ip_addr = socket.gethostbyname(socket.gethostname())
        netmask = ipaddress.IPv4Network(ip_addr).netmask
        return netmask
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def get_default_gateway():
    if sys.platform == 'win32' or 'linux':
        gateways = netifaces.gateways()
        defaults = gateways.get("default")
        if not defaults:
            print(unknown_exception())

        def default_ip(family):
            gw_info = defaults.get(family)
            if not gw_info:
                print(unknown_exception())
            addresses = netifaces.ifaddresses(gw_info[1]).get(family)
            if addresses:
                return addresses[0]["addr"]

        return default_ip(netifaces.AF_INET) or default_ip(netifaces.AF_INET6)
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def is_connected():
    if sys.platform == 'win32' or 'linux':
        try:
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            return True
        except socket.error:
            return False
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def get_hostname():
    if sys.platform == 'win32' or 'linux':
        return socket.gethostname()
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def get_ping_time():
    if sys.platform == 'win32' or 'linux':
        st = speedtest.Speedtest()
        st.get_servers([])
        return str(st.results.ping) + 'ms'
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def get_download_speed():
    if sys.platform == 'win32' or 'linux':
        wifi = speedtest.Speedtest()
        transfer = round(wifi.download())/1000000
        if transfer > 1000:
            return str(transfer/1000) + 'GBps'
        elif 1000 > transfer > 1:
            return str(transfer) + 'Mbps'
        elif transfer < 1:
            return str(transfer*1000) + 'Kbps'
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())


def get_upload_speed():
    if sys.platform == 'win32' or 'linux':
        wifi = speedtest.Speedtest()
        transfer = round(wifi.upload()) / 1000000
        if transfer > 1000:
            return str(transfer / 1000) + 'GBps'
        elif 1000 > transfer > 1:
            return str(transfer) + 'Mbps'
        elif transfer < 1:
            return str(transfer * 1000) + 'Kbps'
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    else:
        print(unsupported_exception())
