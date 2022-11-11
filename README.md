[![pysil](https://github.com/Bamboooz/pysil/blob/master/banner.png?raw=true)](https://github.com/Bamboooz/pysil)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.1.6-yellow)](https://pypi.org/project/pysil/)
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-orange.svg?style=flat-square)](https://www.firsttimersonly.com/)
[![pythonver](https://img.shields.io/badge/python-3.8,%203.9-green)](https://en.wikipedia.org/wiki/Python_(programming_language))
[![os](https://img.shields.io/badge/operating%20system-windows,%20linux-purple)](https://en.wikipedia.org/wiki/Operating_system)
[![docs](https://img.shields.io/badge/docs-here-pink)](https://github.com/Bamboooz/pysil/wiki)

# PySil
Pysil is a free Operating System and Hardware Information library for Python. It provides cross-platform implementation to retrieve system information, such as OS version, processes, memory and CPU usage, disks, devices, sensors, etc.

Current version : 1.1.6

Supported platforms

Windows • Linux

# Supported Features

* Operating system information ( name, version, release, platform, architecture, process list, antivirus )
* CPU information ( model, clockspeed, architecture, temperature, usage, processor number, vendor id)
* GPU information ( id, name, load, memory, temperature )
* RAM information ( memory, manufacturer, form factor, memory type, clockspeed, usage, serial number )
* Motherboard information ( model, serial number, manufacturer, version, node )
* Machine info ( BIOS type [BIOS or UEFI], machine name )
* Disk drives ( list, size, mount type, file system type, mountpoint )
* Network interfaces ( ( IPs ), network parameters, download, upload speed, ping time)
* Display info ( display device, screen resolution, refresh frequency )
* Device info ( usb device list )
* Sound info ( sound device list )
* Battery information ( percentage, is device charging, battery time left )

# Future updates
### Future updates for PySil library:

- [ ] MacOS Support
- [ ] more functions
- [ ] fixing known bugs
- [ ] optimizing code
- [ ] fixing code quality + reducing library weight
- [ ] importing pysil library to other languages ( java, c# )

# Installing
Installing library using python package installer (pip):
```python
pip install pysil # make sure its pysil version 1.1.3 or above,
# because you will have to install all packages manually
```


# Documentation

* [Documentation](https://github.com/Bamboooz/pysil/wiki)
* [Change Log](https://github.com/Bamboooz/pysil/blob/master/CHANGELOG.txt)
* [PyPi page](https://pypi.org/project/pysil/)

# Known Bugs

 * some gpu functions don't work on linux systems
 * Total ram memory will return less by a factor of reserved memory amount.

# Support

* Feel free to contribute. If you want to do so, please contact me ( preferably discord )
* If you found an error, bug or a vulnerability of any sort, please report it to me.
* Contact details:
  - Discord: Bamboooz#8423

# License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
