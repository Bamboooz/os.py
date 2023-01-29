------------------------
## Documentation on getting CPU information using os.py library:
------------------------
### List of CPU functions that os.py library supports:
------------------------

* cpu model
* cpu clockspeed
* cpu architecture
* cpu processor number (physical, logical, total)
* cpu vendor id

------------------------
### Usage of each os.py CPU functions:
------------------------

```python
from os_py import cpu

# getting cpu model
print(cpu.cpu_model()) # example return: AMD Ryzen 7 4800H with Radeon Graphics

# getting cpu clockspeed
print(cpu.cpu_clockspeed()) # example return: 2.9000 GHz

# getting cpu architecture
print(cpu.cpu_architecture()) # example return: X86_64

# getting cpu processor number
print(cpu.cpu_physical_cores()) # example return: 8

# getting cpu processor number
print(cpu.cpu_logical_cores()) # example return: 8

# getting cpu processor number
print(cpu.cpu_total_cores()) # example return: 16

# getting cpu vendor id
print(cpu.cpu_vendor_id()) # example return: AuthenticAMD
```