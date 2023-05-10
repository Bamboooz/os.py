------------------------
## Documentation on getting CPU information using os.py library:
------------------------
### List of CPU functions that os.py library supports:
------------------------

* cpu model
* cpu clockspeed
* cpu architecture
* cpu processor number
* cpu vendor id

------------------------
### Usage of each os.py CPU functions:
------------------------

```python
from ospy import cpu

# getting cpu model
print(cpu.cpu_model())  # example return: AMD Ryzen 7 4800H with Radeon Graphics

# getting cpu total cores
print(cpu.cpu_total_cores())  # example return: 16

# getting cpu clockspeed
print(cpu.cpu_clockspeed())  # example return: 2900Hz

# getting cpu architecture
print(cpu.cpu_architecture())  # example return: AMD64

# getting cpu bits
print(cpu.cpu_bits())  # example return: 64bit

# getting cpu manufacturer
print(cpu.cpu_manufacturer())  # example return: AMD

# getting cpu vendor id
print(cpu.cpu_vendor_id())  # example return: AuthenticAMD
```