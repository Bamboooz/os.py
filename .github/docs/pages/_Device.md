------------------------
## Documentation on getting device information using os.py library:
------------------------
### List of device functions that os.py library supports:
------------------------

* getting usb devices list

------------------------
### Usage of each os.py device functions:
------------------------

```python
from os_py import device

# getting usb devices list
print(device.lst_extern_drives()) # example return:
#  USB\VID_30C9&PID_000E\6&2E165888&0&3
#  USB\VID_25A7&PID_FA61\6&2E165888&0&2
#  USB\ROOT_HUB30\5&78FB108&0&0
#  USB\ROOT_HUB30\5&2C143778&0&0
#  USB\ROOT_HUB30\5&39B4921D&0&0
```