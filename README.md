![pysil](https://github.com/Bamboooz/pysil/blob/master/icon.png?raw=true)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.1.1-yellow)](https://pypi.org/project/pysil/)
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-orange.svg?style=flat-square)](https://www.firsttimersonly.com/)
[![pythonver](https://img.shields.io/badge/python-3.8,%203.9-green)](https://en.wikipedia.org/wiki/Python_(programming_language))
[![os](https://img.shields.io/badge/operating%20system-windows-purple)](https://en.wikipedia.org/wiki/Microsoft_Windows)
[![docs](https://img.shields.io/badge/docs-here-pink)](https://github.com/Bamboooz/pysil/blob/master/pysil/docs.md)

# PySil
Pysil is a free Operating System and Hardware Information library for Python. It provides windows implementation to retrieve system information, such as OS version, processes, memory and CPU usage, disks and partitions, devices, sensors, etc.

Current version : 1.1.1

Supported platforms
---------------------------
Windows

# Supported Features
------------------
* Operating system information ( name, version, release, platform, architecture, process list, antivirus, task list )
* CPU information ( model, clockspeed, architecture, temperature, usage, processor number, vendor id)
* GPU information ( id, name, load, memory, temperature )
* RAM information ( memory, manufacturer, form factor, memory type, clockspeed, usage, serial number )
* Motherboard information ( model, serial number, manufacturer, version, node )
* Machine info ( BIOS type [BIOS or UEFI], machine name )
* Disk drives ( list, size, mount type, file system type, mountpoint )
* Network interfaces ( ( IPs ), network parameters, download, upload speed, ping time)
* Connected displays, graphics
* Battery information (percentage, is_connected, battery time left)
* Sensors ( temperature ) on some hardware

# Future updates
### Future updates for PySil library:

- [ ] Linux support
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
* [Documentation](https://github.com/Bamboooz/pysil/blob/master/pysil/docs.md)
* [Change Log](https://github.com/Bamboooz/pysil/blob/master/CHANGELOG.txt)
* [PyPi page](https://pypi.org/project/pysil/)

# Known Bugs
- if you have some sort of virtual network installed ( for example you have vmware installed ),
all network functions will return the virtual network information, not yours.
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
