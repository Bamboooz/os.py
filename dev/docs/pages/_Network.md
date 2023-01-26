------------------------
## Documentation of getting network information using PySil library:
------------------------
### How to get network information using PySil library in your project:
```python
from pysil import network
print(network.get_ipv4()) # example function
```
```python
from pysil import *
print(network.get_ipv4()) # example function
```
```python
import pysil
print(pysil.network.get_ipv4()) # example function
```
------------------------
### Here is the list of network functions that PySil library supports:
------------------------
* getting ipv4
* getting ipv6
* getting subnet mask
* getting default gateway
* getting information is user connected to the internet
* getting hostname
* getting ping time
* getting download speed
* getting upload speed
------------------------
### Usage of each PySil network functions:
------------------------
```python
# showing only particular data, that is not sensible.
from pysil import network

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
print(network.get_download_speed()) # example return: 93.234Mbps

# getting upload speed
print(network.get_upload_speed()) # example return: 101.245Mbps
```