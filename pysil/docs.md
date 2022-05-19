# Usage
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
print(system.linux_distro()) # example return: ubuntu
print(system.os_architecture()) # example return: AMD64
print(system.process_list()) # example return: process list
print(system.os_antivirus()) # example return: ['Windows Defender', 'Malwarebytes']
print(system.os_uptime()) # example return: 34h
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
print(gpu.gpu_load()) # example return: 0.0%
print(gpu.gpu_free_memory()) # example return: 5991.0MB
print(gpu.gpu_used_memory()) # example return: 0.0MB
print(gpu.gpu_total_memory()) # example return: 6144.0MB
print(gpu.gpu_temperature()) # example return: 45C
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
For gathering storage information use:
( windows: drive_letter = drive letter what you want info about, linux: drive_letter = '' )
```python
from pysil import storage
print(storage.drive_list()) # example return: [{'device': 'C:\\'}, {'device': 'D:\\'}] ( only for windows - linux doesn't have drive letters )
print(storage.get_total_space(drive_letter)) # example return: 476GB
print(storage.get_used_space(drive_letter)) # example return: 269GB
print(storage.get_free_space(drive_letter)) # example return: 207GB
print(storage.get_used_space_percent(drive_letter)) # example return: 56.4%
print(storage.get_drive_fstype(drive_letter)) # example return: NTFS
print(storage.get_drive_mountpoint(drive_letter)) # example return: C:\
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
For gathering device information use:
```python
from pysil import device
print(device.get_usb_list()) # example return:
#  USB\VID_30C9&PID_000E\6&2E165888&0&3
#  USB\VID_25A7&PID_FA61\6&2E165888&0&2
#  USB\ROOT_HUB30\5&78FB108&0&0
#  USB\ROOT_HUB30\5&2C143778&0&0
#  USB\ROOT_HUB30\5&39B4921D&0&0
```
----------------------------------
For gathering sound information use:
```python
from pysil import sound
print(sound.get_audio_devices()) # example return:
#  0 Microsoft Sound Mapper - Input, MME (2 in, 0 out)
#  1 Internal Microphone (AMD Audio , MME (2 in, 0 out)
#  2 Microsoft Sound Mapper - Output, MME (0 in, 2 out)
#  3 Speaker (Realtek(R) Audio), MME (0 in, 2 out)
#  etc...
```
----------------------------------
For gathering network information use:
```python
# showing only particular data, that is not sensible.
from pysil import network
print(network.get_ipv4())
print(network.get_ipv6())
print(network.get_subnet_mask())
print(network.get_default_gateway())
print(network.is_connected()) # example return: True
print(network.get_hostname())
print(network.get_ping_time()) # example return: 0ms
print(network.get_download_speed()) # example return: 93.234Mbps
print(network.get_upload_speed()) # example return: 101.245Mbps
```
----------------------------------