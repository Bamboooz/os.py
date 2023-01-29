------------------------
## Documentation on getting network information using os.py library:
------------------------

------------------------
### List of network functions that os.py library supports:
------------------------

* getting ipv4
* getting ipv6
* getting subnet mask
* getting default gateway
* is user connected to the internet
* getting hostname
* getting ping time
* getting download speed
* getting upload speed

------------------------
### Usage of each os.py network functions:
------------------------

```python
# showing only particular data, that is not sensible.
from os_py import network

# getting ipv4
print(network.get_ipv4())

# getting ipv6
print(network.get_ipv6())

# getting subnet mask
print(network.get_subnet_mask())

# getting default gateway
print(network.get_default_gateway())

# getting information is user connected to the internet
print(network.is_connected()) # example return: True

# getting hostname
print(network.get_hostname())

# getting ping time
print(network.get_ping_time()) # example return: 0ms

# getting download speed
print(network.user_download_speed()) # example return: 93.234Mbps

# getting upload speed
print(network.user_upload_speed()) # example return: 101.245Mbps
```