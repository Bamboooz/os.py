------------------------
## Documentation on getting display information using os.py library:
------------------------

------------------------
### List of display functions that os.py library supports:
------------------------

* getting display devices
* getting screen resolution
* getting screen refresh frequency

------------------------
### Usage of each os.py display functions:
------------------------

```python
from os_py import display

# getting display devices
print(display.display_device()) # example return: ('\\\\.\\DISPLAY1', 'AMD Radeon(TM) Graphics')

# getting screen resolution
print(display.screen_resolution()) # example return: 1920x1080

# getting screen refresh frequency
print(display.screen_refresh_frequency()) # example return: 144Hz
```