------------------------
## Documentation on getting machine information using os.py library:
------------------------
### List of machine functions that os.py library supports:
------------------------

* getting machine name
* getting boot type ( BIOS or UEFI )

------------------------
### Usage of each os.py machine functions:
------------------------

```python
from os_py import machine

# getting machine name
print(machine.machine_name()) # example return: DESKTOP-236TBJV

# getting bios type ( BIOS or UEFI )
print(machine.boot_type()) # example return: UEFI
```