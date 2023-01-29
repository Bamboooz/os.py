------------------------
## Documentation on getting motherboard information using os.py library:
------------------------

------------------------
### List of motherboard functions that os.py library supports:
------------------------

* getting motherboard model
* getting motherboard manufacturer
* getting motherboard serial number
* getting motherboard version
* getting motherboard node

------------------------
### Usage of each os.py motherboard functions:
------------------------

```python
from os_py import motherboard

# getting motherboard model
print(motherboard.model()) # example return: 8786

# getting motherboard manufacturer
print(motherboard.manufacturer()) # example return: HP

# getting motherboard serial number
print(motherboard.serial_number()) # example return: 31444335-3530-4331-5736-6C02E073D649

# getting motherboard version
print(motherboard.version()) # example return: 22.54

# getting motherboard node
print(motherboard.node()) # example return: 145253501163834
```