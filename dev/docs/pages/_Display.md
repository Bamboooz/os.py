------------------------
## Documentation of getting display information using PySil library:
------------------------
### How to get display information using PySil library in your project:
```python
from pysil import display
print(display.screen_resolution()) # example function
```
```python
from pysil import *
print(display.screen_resolution()) # example function
```
```python
import pysil
print(pysil.display.screen_resolution()) # example function
```
------------------------
### Here is the list of display functions that PySil library supports:
------------------------
* getting display devices
* getting screen resolution
* getting screen refresh frequency
------------------------
### Usage of each PySil display functions:
------------------------
```python
from pysil import display

# getting display devices
print(display.display_device()) # example return: ('\\\\.\\DISPLAY1', 'AMD Radeon(TM) Graphics')

# getting screen resolution
print(display.screen_resolution()) # example return: 1920x1080

# getting screen refresh frequency
print(display.screen_refresh_frequency()) # example return: 144Hz
``