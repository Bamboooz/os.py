<p align="center">
	<br>
	<img src="https://github.com/Bamboooz/pysil/blob/master/banner.png?raw=true">
	<br>
	<br>
	<b>os.py</b>: Python library to know your operating system better.
	<br>
</p>

<p align="center">
	<a href="https://opensource.org/licenses/MIT">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg"/>
	</a>
	<a href="https://pypi.org/project/pysil/">
		<img src="https://img.shields.io/badge/version-1.1.7-yellow"/>
	</a>
	<a href="https://www.firsttimersonly.com/">
		<img src="https://img.shields.io/badge/first--timers--only-friendly-orange.svg?style=flat-square"/>
	</a>
  <a href="https://en.wikipedia.org/wiki/Python_(programming_language)">
		<img src="https://img.shields.io/badge/python-3.8,%203.9-green"/>
	</a>
  <a href="https://en.wikipedia.org/wiki/Operating_system">
		<img src="https://img.shields.io/badge/operating%20system-windows,%20linux,%20macOS-purple"/>
	</a>
  <a href="https://github.com/Bamboooz/pysil/wiki">
		<img src="https://img.shields.io/badge/docs-here-pink"/>
	</a>
  
  <br>
  <br>
</p>

## About

os.py is a free Operating System and Hardware Information library for Python. It provides cross-platform implementation to retrieve system information, such as OS version, processes, memory and CPU usage, disks, devices, sensors, etc.

Current version : 1.1.7

## Supported platforms

 •ㅤWindowsㅤ•ㅤLinuxㅤ•ㅤmacOSㅤ•

## Example usage

```python
from os_py import system, cpu

print(system.os_name())
 >> Windows

print(cpu.cpu_model())
 >> AMD Ryzen 7 4800H with Radeon Graphics
```

## Supported Features

A complete list of [os.py](https://github.com/Bamboooz/os.py) functions:

 * Operating system information
 * CPU information
 * GPU information
 * RAM information
 * Motherboard information
 * Machine info
 * Physical drives
 * Network interfaces
 * Display info
 * Device info
 * Sound info
 * Battery information

To get more detailed information about specific os.py functions visit [Detailed os.py Functions](https://github.com/Bamboooz/pysil/wiki/PySil-Functions).

## Future updates

### Future updates for os.py library:

 - [ ] Support for other platforms
 - [ ] More functions
 - [ ] Fixing known bugs
 - [ ] Optimizing code
 - [ ] Fixing code quality + reducing library weight
 - [ ] Importing os.py library to other languages (java, c#)

## Installing

Installing library using python package installer (pip):
```python
pip install os_py
# make sure its os.py version 1.1.3 or above,
# all versions below are deprecated and are not working
```

## Documentation

 * [Documentation](https://github.com/Bamboooz/os.py/wiki)
 * [Change Log](https://github.com/Bamboooz/os.py/blob/master/CHANGELOG.txt)
 * [PyPi page](https://pypi.org/project/os.py/)

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
