![pysil](https://github.com/Bamboooz/pysil/blob/master/banner.png?raw=true)

# PySil
PySil is simple, but kind of useful python library to gather:
  - system information
  - hardware information
  - network information

# Compatibility 
Current PySil version: 1.0.7

Currently most of PySil's library functions are only supported
by Windows, but I am currently working on Linux support.

Linux support almost done! Functions to do: RAM, GPU, motherboard and storage.

I've been testing and coding this library on python 3.8 and 3.9,
but I have no idea if it works on other versions too.

Required python pacakges to run pysil library are in the requirements.txt file.

# ToDo List
### ToDo list for PySil library:

- [ ] Linux Support
- [ ] MacOS Support
- [ ] more functions
- [ ] fixing ram amount bug
- [ ] fixing virtual network bug
- [ ] fixing code quality + reducing library weight
- [ ] importing pysil library to other languages ( java, c# )

# Installing
Pip install:
```python
pip install pysil # make sure its pysil version 1.0.5 or above, cause it wont work then
```

# Usage
Commands in PySil library are the same for every single
operating system, and you don't have to change anything
in import etc. - our library will automaticly detect
your operating system and apply correct code for you.

For gathering system information use:
```python
from pysil import system
print(system.os_name()) # example return: Windows
print(system.os_version()) # example return: 19044 
print(system.os_platform()) # example return: Windows-10-10.0.19044-SP0
print(system.os_release()) # example return: 10
print(system.os_architecture()) # example return: AMD64
print(system.linux_distro()) # example return: ubuntu ( works only on linux )
```

For gathering CPU information use:
```python
from pysil import cpu
print(cpu.cpu_model()) # example return: AMD Ryzen 7 4800H with Radeon Graphics
print(cpu.cpu_clockspeed()) # example return: 2.9000 GHz
print(cpu.cpu_architecture()) # example return: X86_64
print(cpu.cpu_processor_number()) # example return: 16
print(cpu.cpu_usage()) # example return: 17.5%
print(cpu.cpu_temperature()) # example return: 80C
print(cpu.cpu_vendor_id()) # example return: AuthenticAMD
```

For gathering GPU information use:
```python
from pysil import gpu
print(gpu.gpu_id()) # example return: 0
print(gpu.gpu_name()) # example return: NVIDIA GeForce GTX 1660 Ti
print(gpu.gpu_load()) # example return: 0.0%
print(gpu.gpu_free_memory()) # example return: 5991.0MB
print(gpu.gpu_used_memory()) # example return: 0.0MB
print(gpu.gpu_total_memory()) # example return: 6144.0MB
print(gpu.gpu_temperature()) # example return: 45C
print(gpu.get_uuid()) # example return: GPU-7acefeea-cbae-0e2f-3c6f-10540fb3ada6
```

For gathering RAM information use:
```python
from pysil import ram
print(ram.ram_total_memory()) # example return: 15.362663269042969 GB
print(ram.ram_manufacturer()) # example return: Hynix
print(ram.ram_serial_number()) # example return: 543B8173
print(ram.ram_memory_type()) # example return: DDR4
print(ram.ram_form_factor()) # example return: SODIMM
print(ram.ram_clockspeed()) # example return: 3200Hz
print(ram.ram_usage()) # example return: 54.7%
```

For gathering storage information use: ( as drive_letter use the letter of the drive you want to get info about )
```python
from pysil import storage
print(storage.drive_list()) # example return: [{'device': 'C:\\'}, {'device': 'D:\\'}] ( only for windows - linux doesnt have drive letters )
print(storage.get_total_space()) # example return: 476GB
print(storage.get_used_space()) # example return: 269GB
print(storage.get_free_space()) # example return: 207GB
print(storage.get_used_space_percent()) # example return: 56.4%
print(storage.get_drive_fstype(drive_letter)) # example return: NTFS ( only for windows - linux doesnt have drive letters )
print(storage.get_drive_mountpoint(drive_letter)) # example return: C:\ ( only for windows - linux doesnt have drive letters )
```

For gathering motherboard information use:
```python
from pysil import motherboard
print(motherboard.motherboard_model()) # example return: 8786
print(motherboard.motherboard_manufacturer()) # example return: HP
print(motherboard.motherboard_serial_number()) # example return: 31444335-3530-4331-5736-6C02E073D649
print(motherboard.motherboard_version()) # example return: 22.54
print(motherboard.motherboard_node()) # example return: 145253501163834
```

For gathering machine information use:
```python
from pysil import machine
print(machine.machine_name()) # example return: DESKTOP-236TBJV
print(machine.bios_type()) # example return: UEFI
```

For gathering network information use:
```python
# not showing example return cause i might accidentaly leak someones data.
from pysil import network
print(network.get_ipv4())
print(network.get_ipv6())
print(network.get_subnet_mask())
print(network.get_default_gateway())
print(network.is_connected()) # example return: True
print(network.get_hostname())
```

# Known Bugs
- if you have some sort of virtual network installed ( for example you have vmware installed ),
all network functions will return the virtual netwrok information, not yours.
- total ram memory will return not correct amount, it returns a little bit less than you have ( about 0.7 GB ).

# Notes
1) Some of PySil's library functions require to be run as administrator,
because some of them are using libraries like wmi, so if you are
getting an unexpected error, try running your IDE as administrator,
and restart your script.

2) Some of PySil's library functions might have an error, and if you are having one
for example function is returning wrong data, or function is just not working
please contact me.
 
3) Some functions might need few seconds ( depending on your computer specs ) to return the data, because it needs to access
files, read them, get needed data and then return it, so be patient. If it is taking longer than about 8sec then please contact me.

4) Feel free to contribute, I will appriciate it for sure. If you want to do so, please contact me ( preferably discord )

5) If you found an error or vurnability of any sort, please report it to me.

6) Contact details:
  - E-mail: bambusixmc@gmail.com
  - Discord: Bamboooz#8423
