------------------------
## Documentation on getting RAM information using os.py library:
------------------------

------------------------
### List of RAM functions that os.py library supports:
------------------------

* ram total memory
* ram manufacturer
* ram serial number
* ram memory type
* ram form factor
* ram clockspeed
* ram usage

------------------------
### Usage of each os.py RAM functions:
------------------------

```python
from os_py import ram

# getting ram total memory
print(ram.ram_total_memory()) # example return: 15.362663269042969 GB

# getting ram manufacturer
print(ram.ram_manufacturer()) # example return: Hynix

# getting ram serial number
print(ram.ram_serial_number()) # example return: 543B8173

# getting ram memory type
print(ram.ram_memory_type()) # example return: DDR4

# getting ram form factor
print(ram.ram_form_factor()) # example return: SODIMM

# getting ram clockspeed
print(ram.ram_clockspeed()) # example return: 3200Hz

# getting ram usage
print(ram.ram_usage()) # example return: 54.7%
```