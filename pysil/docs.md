# Usage
----------------------------------

Commands in PySil library are the same for every single
operating system, and you don't have to change anything
in import etc. - our library will automatically detect
your operating system and apply correct code for you.

----------------------------------

Required python packages to run pysil library are in the requirements.txt file.

----------------------------------

For gathering system information use:
```python
from pysil import system
print(system.os_name()) # example return: Windows
print(system.os_version()) # example return: 19044 
print(system.os_platform()) # example return: Windows-10-10.0.19044-SP0
print(system.os_release()) # example return: 10
print(system.os_architecture()) # example return: AMD64
print(system.linux_distro()) # example return: ubuntu ( works only on linux )
print(system.process_list()) # example return: process list
print(system.os_antivirus()) # example return: ['Windows Defender', 'Malwarebytes']
```
----------------------------------
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
----------------------------------
For gathering GPU information use:
```python
from pysil import gpu
print(gpu.gpu_id()) # example return: 0
print(gpu.gpu_name()) # example return: NVIDIA GeForce GTX 1660 Ti
print(gpu.gpu_load()) # example return: 0.0% # does not work on linux, i don't know why
print(gpu.gpu_free_memory()) # example return: 5991.0MB # does not work on linux, i don't know why
print(gpu.gpu_used_memory()) # example return: 0.0MB # does not work on linux, i don't know why
print(gpu.gpu_total_memory()) # example return: 6144.0MB # does not work on linux, i don't know why
print(gpu.gpu_temperature()) # example return: 45C # does not work on linux, i don't know why
```
----------------------------------
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
----------------------------------
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
----------------------------------
For gathering motherboard information use:
```python
from pysil import motherboard
print(motherboard.motherboard_model()) # example return: 8786
print(motherboard.motherboard_manufacturer()) # example return: HP
print(motherboard.motherboard_serial_number()) # example return: 31444335-3530-4331-5736-6C02E073D649
print(motherboard.motherboard_version()) # example return: 22.54
print(motherboard.motherboard_node()) # example return: 145253501163834
```
----------------------------------
For gathering battery information use:
```python
from pysil import battery
print(battery.battery_percentage()) # example return: 57%
print(battery.is_plugged_in()) # example return: True
print(battery.battery_time_left()) # example return: 1.3h
```
----------------------------------
For gathering display information use:
```python
from pysil import display
print(display.display_device()) # example return: ('\\\\.\\DISPLAY1', 'AMD Radeon(TM) Graphics')
print(display.screen_resolution()) # example return: 1920x1080
print(display.screen_refresh_frequency()) # example return: 144Hz
```
----------------------------------
For gathering machine information use:
```python
from pysil import machine
print(machine.machine_name()) # example return: DESKTOP-236TBJV
print(machine.bios_type()) # example return: UEFI
```
----------------------------------
For gathering network information use:
```python
# not showing example return because I might accidentally leak someone's data.
from pysil import network
print(network.get_ipv4())
print(network.get_ipv6())
print(network.get_subnet_mask())
print(network.get_default_gateway())
print(network.is_connected()) # example return: True
print(network.get_hostname())
```
----------------------------------