------------------------
## Documentation of getting sound information using PySil library:
------------------------
### How to get sound information using PySil library in your project:
```python
from pysil import sound
print(sound.get_audio_devices()) # example function
```
```python
from pysil import *
print(sound.get_audio_devices()) # example function
```
```python
import pysil
print(pysil.sound.get_audio_devices()) # example function
```
------------------------
### Here is the list of sound functions that PySil library supports:
------------------------
* getting audio devices list
------------------------
### Usage of each PySil sound functions:
------------------------
```python
from pysil import sound

# getting audio devices
print(sound.get_audio_devices()) # example return:
#  0 Microsoft Sound Mapper - Input, MME (2 in, 0 out)
#  1 Internal Microphone (AMD Audio , MME (2 in, 0 out)
#  2 Microsoft Sound Mapper - Output, MME (0 in, 2 out)
#  3 Speaker (Realtek(R) Audio), MME (0 in, 2 out)
#  etc...
```