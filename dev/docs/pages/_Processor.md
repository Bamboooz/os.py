------------------------
## Documentation of getting CPU information using PySil library:
------------------------
### How to get CPU information using PySil library in your project:
```python
from pysil import cpu
print(cpu.cpu_model()) # example function
```
```python
from pysil import *
print(cpu.cpu_model()) # example function
```
```python
import pysil
print(pysil.cpu.cpu_model()) # example function
```
------------------------
### Here is the list of CPU functions that PySil library supports:
------------------------
* cpu model
* cpu clockspeed
* cpu architecture
* cpu processor number
* cpu usage
* cpu temperature
* cpu vendor id
------------------------
### Usage of each PySil CPU functions:
------------------------
```python
from pysil import cpu

# getting cpu model
print(cpu.cpu_model()) # example return: AMD Ryzen 7 4800H with Radeon Graphics

# getting cpu clockspeed
print(cpu.cpu_clockspeed()) # example return: 2.9000 GHz

# getting cpu architecture
print(cpu.cpu_architecture()) # example return: X86_64

# getting cpu processor number
print(cpu.cpu_processor_number()) # example return: 16

# getting cpu usage
print(cpu.cpu_usage()) # example return: 17.5%

# getting cpu temperature
print(cpu.cpu_temperature()) # example return: 80C

# getting cpu vendor id
print(cpu.cpu_vendor_id()) # example return: AuthenticAMD
```