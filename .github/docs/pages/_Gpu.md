------------------------
## Documentation on getting GPU information using os.py library:
------------------------
### List of GPU functions that os.py library supports:
------------------------

* gpu id
* gpu name
* gpu serial number
* gpu uuid
* gpu total memory
* gpu free memory
* gpu used memory
* gpu display mode
* gpu active display

------------------------
### Usage of each os.py GPU functions:
------------------------

```python
from ospylib import gpu

# getting gpu id
print(gpu().gpu_id())  # example return: 0

# getting gpu model
print(gpu().gpu_name())  # example return: NVIDIA GeForce GTX 1660 Ti

# getting gpu serial number
print(gpu().gpu_serial_number())  # example return: [N/A]

# getting gpu uuid
print(gpu().gpu_uuid())  # example return: GPU-7acefeea-cbae-0e2f-3c6f-10540fb3ada6

# getting gpu total memory
print(gpu().gpu_memory_total())  # example return: 6144MB

# getting gpu free memory
print(gpu().gpu_memory_free())  # example return: 6144MB

# getting gpu used memory
print(gpu().gpu_memory_used())  # example return: 0MB

# getting gpu display mode
print(gpu().gpu_display_mode())  # example return: Disabled

# getting gpi active display
print(gpu().gpu_display_active())  # example return: Disabled
```