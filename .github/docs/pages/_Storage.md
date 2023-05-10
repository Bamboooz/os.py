------------------------
## Documentation on getting storage information using os.py library:
-------------------------
### List of storage functions that os.py library supports:
------------------------

* getting list of drives
* getting drive total space
* getting drive used space
* getting drive free space
* getting drive used space in %

------------------------
### Usage of each os.py storage functions:
------------------------

```python
from ospy import storage

# as for drive_letter you insert drive letter you want to get information about, example: 'C'
# default drive letter for windows 'C', and for linux its '/'

print(storage.drive_list())
# example return: [{'device': 'C:\\'}, {'device': 'D:\\'}]

# getting drive total space
print(storage().get_total_space())  # example return: 476GB

# getting drive used space
print(storage().get_used_space())  # example return: 269GB

# getting drive free space
print(storage().get_free_space())  # example return: 207GB

# getting drive used space ( in % )
print(storage().get_used_space_percent())  # example return: 56.4%
```