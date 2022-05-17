![pysil](https://github.com/Bamboooz/pysil/blob/master/icon.png?raw=true)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Version](https://img.shields.io/badge/version-1.0.9-yellow)
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-orange.svg?style=flat-square)](https://www.firsttimersonly.com/)
![pythonver](https://img.shields.io/badge/python-3.9-green)
![os](https://img.shields.io/badge/operating%20system-windows,%20linux-purple)
[![docs](https://img.shields.io/badge/docs-here-pink)](https://github.com/Bamboooz/pysil/blob/master/pysil/docs.md)

# PySil
Pysil is a free Operating System and Hardware Information library for Python. It provides a cross-platform implementation to retrieve system information, such as OS version, processes, memory and CPU usage, disks and partitions, devices, sensors, etc.

Current version : 1.0.9

# Supported Features
------------------
* Operating system information ( name, distribution, release etc. )
* CPU information ( model, clockspeed, temperature, architecture etc. )
* GPU information ( id, name, load, memory, temperature etc. )
* RAM information ( memory, manufacturer, form factor, memory type, clockspeed, usage etc. )
* Physical and virtual memory used/available
* Mounted filesystems (type, total space)
* Motherboard information ( model, serial number, manufacturer, version, node )
* Machine info ( BIOS type [BIOS or UEFI], machine name )
* Disk drives ( model, serial, size )
* Network interfaces ( IPs ), network parameters
* Connected displays, graphics
* Battery information (percentage, is_connected, battery time left)
* Sensors ( temperature ) on some hardware

# Future updates
### Future updates for PySil library:

- [ ] Full Linux support
- [ ] MacOS Support
- [ ] more functions
- [ ] fixing ram amount bug
- [ ] fixing virtual network bug
- [ ] fixing code quality + reducing library weight
- [ ] importing pysil library to other languages ( java, c# )

# Installing
Installing library using python package installer (pip):
```python
pip install pysil # make sure its pysil version 1.0.5 or above, cause it wont work then
```

# Documentation
* [DOCS](https://github.com/Bamboooz/pysil/blob/master/pysil/docs.md)
* [Change Log](https://github.com/Bamboooz/pysil/blob/master/CHANGELOG.txt)

# Known Bugs
- if you have some sort of virtual network installed ( for example you have vmware installed ),
all network functions will return the virtual network information, not yours.
- gpu total, used, free memory and gpu temp on linux in returning none or errors.
- total ram memory will return not correct amount, it returns a little less than you have ( about 0.7 GB ).

# Support
----------------------------------
* Feel free to contribute, I will appreciate it for sure. If you want to do so, please contact me ( preferably discord )
* If you found an error or vulnerability of any sort, please report it to me.
* Contact details:
  - E-mail: bambusixmc@gmail.com
  - Discord: Bamboooz#8423

# License
-------
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
