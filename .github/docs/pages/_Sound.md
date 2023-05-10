------------------------
## Documentation on getting sound information using os.py library:
------------------------
### Sound functions that os.py library supports:
------------------------

* getting audio devices list

------------------------
### Usage of each os.py sound functions:
------------------------

```python
from ospy import sound

# getting audio devices
print(sound.get_sound_devices())  # example return:
#  0 Microsoft Sound Mapper - Input, MME (2 in, 0 out)
#  1 Internal Microphone (AMD Audio , MME (2 in, 0 out)
#  2 Microsoft Sound Mapper - Output, MME (0 in, 2 out)
#  3 Speaker (Realtek(R) Audio), MME (0 in, 2 out)
#  etc...
```