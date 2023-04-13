------------------------
## Documentation on getting system information using os.py library:
------------------------
### System functions that os.py library supports:
------------------------

* operating system name
* operating system version
* operating system platform
* operating system release
* linux distribution
* operating system architecture

------------------------
### Usage of each os.py system functions:
------------------------

```python
from os_py import system

# getting operating system name
print(system.os_name()) # example return: Windows

# getting operating system version
print(system.os_version()) # example return: 19044

# getting operating system platform
print(system.os_platform()) # example return: Windows-10-10.0.19044-SP0

# getting operating system release
print(system.os_release()) # example return: 10

# getting machine architecture
print(system.machine_architecture()) # example return: AMD64

# getting linux distribution (works only on linux systems)
print(system.linux_distro()) # example return: Ubuntu

# getting operating system architecture
print(system.os_architecture()) # example return: 64bit
```