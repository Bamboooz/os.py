------------------------
## Documentation on getting battery information using os.py library:
------------------------

### List of battery functions that os.py library supports:
------------------------

* getting battery percentage
* getting information is battery plugged in
* getting battery time left

------------------------
### Usage of each os.py battery functions:
------------------------

```python
from os_py import battery

# getting battery percentage
print(battery.battery_percentage()) # example return: 57%

# getting information is battery plugged in
print(battery.is_plugged_in()) # example return: True

# getting battery time left
print(battery.battery_time_left()) # example return: 1.3h
```