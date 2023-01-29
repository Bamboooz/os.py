------------------------
## Documentation on getting GPU information using os.py library:
------------------------

------------------------
### List of GPU functions that os.py library supports:
------------------------

* gpu id
* gpu name
* gpu load
* gpu free memory
* gpu used memory
* gpu total memory
* gpu temperature

------------------------
### Usage of each os.py GPU functions:
------------------------

```python
from os_py import gpu

# getting gpu id
print(gpu.gpu_id()) # example return: 0

# getting gpu model
print(gpu.gpu_name()) # example return: NVIDIA GeForce GTX 1660 Ti

# getting gpu usage
print(gpu.gpu_load()) # example return: 0.0%

# getting gpu free memory
print(gpu.gpu_free_memory()) # example return: 5991.0MB

# getting gpu used memory
print(gpu.gpu_used_memory()) # example return: 0.0MB

# getting gpu total memory
print(gpu.gpu_total_memory()) # example return: 6144.0MB

# getting gpu temperature
print(gpu.gpu_temperature()) # example return: 45C
```