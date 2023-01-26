------------------------
## Documentation of getting motherboard information using PySil library:
------------------------
### How to get motherboard information using PySil library in your project:
```python
from pysil import motherboard
print(motherboard.motherboard_model()) # example function
```
```python
from pysil import *
print(motherboard.motherboard_model()) # example function
```
```python
import pysil
print(pysil.motherboard.motherboard_model()) # example function
```
------------------------
### Here is the list of motherboard functions that PySil library supports:
------------------------
* getting motherboard model
* getting motherboard manufacturer
* getting motherboard serial number
* getting motherboard version
* getting motherboard node
------------------------
### Usage of each PySil motherboard functions:
------------------------
```python
from pysil import motherboard

# getting motherboard model
print(motherboard.motherboard_model()) # example return: 8786

# getting motherboard manufacturer
print(motherboard.motherboard_manufacturer()) # example return: HP

# getting motherboard serial number
print(motherboard.motherboard_serial_number()) # example return: 31444335-3530-4331-5736-6C02E073D649

# getting motherboard version
print(motherboard.motherboard_version()) # example return: 22.54

# getting motherboard node
print(motherboard.motherboard_node()) # example return: 145253501163834
```