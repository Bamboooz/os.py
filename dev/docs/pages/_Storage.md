------------------------
## Documentation of getting storage information using PySil library:
------------------------
### How to get storage information using PySil library in your project:
```python
from pysil import storage
print(storage.get_total_space()) # example function
```
```python
from pysil import *
print(storage.get_total_space()) # example function
```
```python
import pysil
print(pysil.storage.get_total_space()) # example function
```
------------------------
### Here is the list of storage functions that PySil library supports:
------------------------
* getting list of drives
* getting drive total space
* getting drive used space
* getting drive free space
* getting drive used space in %
* getting drive file system type
* getting drive mountpoint
------------------------
### Usage of each PySil storage functions:
------------------------
```python
from pysil import storage

# as for drive_letter you insert drive letter you want to get information about
# ( only for windows, linux doesn't support drive letters, example: 'C' )
# and as for linux you leave drive_letter empty

# getting drive list  ( only for windows )
print(storage.drive_list())
# example return: [{'device': 'C:\\'}, {'device': 'D:\\'}]

# getting drive total space
print(storage.get_total_space(drive_letter)) # example return: 476GB

# getting drive used space
print(storage.get_used_space(drive_letter)) # example return: 269GB

# getting drive free space
print(storage.get_free_space(drive_letter)) # example return: 207GB

# getting drive used space ( in % )
print(storage.get_used_space_percent(drive_letter)) # example return: 56.4%

# getting drive file system type ( only for windows )
print(storage.get_drive_fstype(drive_letter)) # example return: NTFS

# getting drive mountpoint ( only for windows )
print(storage.get_drive_mountpoint(drive_letter)) # example return: C:\
```