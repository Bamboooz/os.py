------------------------
## Documentation of getting device information using PySil library:
------------------------
### How to get device information using PySil library in your project:
```python
from pysil import device
print(device.get_usb_list()) # example function
```
```python
from pysil import *
print(device.get_usb_list()) # example function
```
```python
import pysil
print(pysil.device.get_usb_list()) # example function
```
------------------------
### Here is the list of device functions that PySil library supports:
------------------------
* getting usb devices list
------------------------
### Usage of each PySil device functions:
------------------------
```python
from pysil import device

# getting usb devices list
print(device.get_usb_list()) # example return:
#  USB\VID_30C9&PID_000E\6&2E165888&0&3
#  USB\VID_25A7&PID_FA61\6&2E165888&0&2
#  USB\ROOT_HUB30\5&78FB108&0&0
#  USB\ROOT_HUB30\5&2C143778&0&0
#  USB\ROOT_HUB30\5&39B4921D&0&0
```