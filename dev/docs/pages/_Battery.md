------------------------
## Documentation of getting battery information using PySil library:
------------------------
### How to get battery information using PySil library in your project:
```python
from pysil import battery
print(battery.battery_percentage()) # example function
```
```python
from pysil import *
print(battery.battery_percentage()) # example function
```
```python
import pysil
print(pysil.battery.battery_percentage()) # example function
```
------------------------
### Here is the list of battery functions that PySil library supports:
------------------------
* getting battery percentage
* getting information is battery plugged in
* getting battery time left
------------------------
### Usage of each PySil battery functions:
------------------------
```python
from pysil import battery

# getting battery percentage
print(battery.battery_percentage()) # example return: 57%

# getting information is battery plugged in
print(battery.is_plugged_in()) # example return: True

# getting battery time left
print(battery.battery_time_left()) # example return: 1.3h
```