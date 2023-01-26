------------------------
## Documentation of getting machine information using PySil library:
------------------------
### How to get machine information using PySil library in your project:
```python
from pysil import machine
print(machine.machine_name()) # example function
```
```python
from pysil import *
print(machine.machine_name()) # example function
```
```python
import pysil
print(pysil.machine.machine_name()) # example function
```
------------------------
### Here is the list of machine functions that PySil library supports:
------------------------
* getting machine name
* getting bios type ( BIOS or UEFI )
------------------------
### Usage of each PySil machine functions:
------------------------
```python
from pysil import machine

# getting machine name
print(machine.machine_name()) # example return: DESKTOP-236TBJV

# getting bios type ( BIOS or UEFI )
print(machine.bios_type()) # example return: UEFI
```