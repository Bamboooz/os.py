import ipaddress
import socket
import netifaces
import speedtest


def get_ipv4():
    hostname = socket.gethostname()
    ipv4 = socket.gethostbyname(hostname)
    return ipv4


def get_ipv6():
    alladdr = socket.getaddrinfo(socket.gethostname(), 0)
    ip6 = filter(
        lambda x: x[0] == socket.AF_INET6,  # means its ip6
        alladdr
    )
    return list(ip6)[0][4][0]


def get_subnet_mask():
    ip_addr = socket.gethostbyname(socket.gethostname())
    netmask = ipaddress.IPv4Network(ip_addr).netmask
    return netmask


def get_default_gateway():
    gateways = netifaces.gateways()
    defaults = gateways.get("default")

    if not defaults:
        return None

    def default_ip(family):
        gw_info = defaults.get(family)

        if not gw_info:
            return None

        addresses = netifaces.ifaddresses(gw_info[1]).get(family)
        if addresses:
            return addresses[0]["addr"]

    return default_ip(netifaces.AF_INET) or default_ip(netifaces.AF_INET6)


def is_connected():
    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except socket.error:
        return False


def get_hostname():
    return socket.gethostname()


def get_ping_time():
    st = speedtest.Speedtest()
    st.get_servers([])
    return str(st.results.ping) + 'ms'


def get_download_speed():
    wifi = speedtest.Speedtest()
    transfer = round(wifi.download())/1000000
    if transfer > 1000:
        return str(transfer/1000) + 'GBps'
    elif 1000 > transfer > 1:
        return str(transfer) + 'Mbps'
    elif transfer < 1:
        return str(transfer*1000) + 'Kbps'


def get_upload_speed():
    wifi = speedtest.Speedtest()
    transfer = round(wifi.upload()) / 1000000
    if transfer > 1000:
        return str(transfer / 1000) + 'GBps'
    elif 1000 > transfer > 1:
        return str(transfer) + 'Mbps'
    elif transfer < 1:
        return str(transfer * 1000) + 'Kbps'
