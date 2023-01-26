------------------------
## Documentation of getting system information using PySil library:
------------------------
### How to get system information using PySil library in your project:
```python
from pysil import system
print(system.os_name()) # example function
```
```python
from pysil import *
print(system.os_name()) # example function
```
```python
import pysil
print(pysil.system.os_name()) # example function
```
------------------------
### Here is the list of system functions that PySil library supports:
------------------------
* operating system name
* operating system version
* operating system platform (full version name)
* operating system release (shortened version name)
* linux distribution
* operating system architecture
* process list
* installed antiviruses
* operating system uptime
------------------------
### Usage of each PySil system functions:
------------------------
```python
from pysil import system

# getting operating system name
print(system.os_name()) # example return: Windows

# getting operating system version
print(system.os_version()) # example return: 19044

# getting operating system platform
print(system.os_platform()) # example return: Windows-10-10.0.19044-SP0

# getting operating system release
print(system.os_release()) # example return: 10

# getting linux distribution ( works only on linux )
print(system.linux_distro()) # example return: Ubuntu

# getting operating system architecture
print(system.os_architecture()) # example return: AMD64

# getting operating system process list
print(system.process_list()) # example return:
# Image Name                     PID Session Name        Session#    Mem Usage
# ========================= ======== ================ =========== ============
# System Idle Process              0 Services                   0          8 K
# System                           4 Services                   0     10˙416 K
# Registry                       172 Services                   0     48˙908 K
# smss.exe                       584 Services                   0        516 K
# csrss.exe                      828 Services                   0      2˙756 K
# etc...

# getting installed antivirus softwares
print(system.os_antivirus()) # example return: ['Windows Defender', 'Malwarebytes']

# getting operating system uptime
print(system.os_uptime()) # example return: 34h
```