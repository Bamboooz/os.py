<div align="center">

![os.py](https://i.ibb.co/WPD4fyr/banner.png)

-----------------

[![](https://img.shields.io/github/v/release/Bamboooz/os.py?color=yellow?style=flat-square)](https://github.com/Bamboooz/os.py/releases/)
[![](https://img.shields.io/badge/python-3.6%20and%20newer-brightgreen)](https://en.wikipedia.org/wiki/Python_(programming_language))
[![](https://img.shields.io/badge/operating%20system-windows-purple)](https://en.wikipedia.org/wiki/Operating_system)
[![](https://www.aschey.tech/tokei/github/Bamboooz/os.py?style=flat-square)](https://github.com/Bamboooz/os.py)
![](https://img.shields.io/github/languages/code-size/Bamboooz/os.py?color=red)
[![](https://img.shields.io/badge/License-BSD--3--Clause-blue)](https://opensource.org/license/bsd-3-clause/)

-----------------

[**Home**](https://github.com/Bamboooz/os.py)⠀
[**Install**](https://github.com/Bamboooz/os.py#installation)⠀
[**Documentation**](https://github.com/Bamboooz/os.py/wiki)⠀
[**Contributing**](https://github.com/Bamboooz/os.py/blob/master/CONTRIBUTING.md)⠀
[**Download**](https://pypi.org/project/os.py#files)⠀
[**Security**](https://github.com/Bamboooz/os.py/blob/master/SECURITY.md)⠀
[**License**](https://github.com/Bamboooz/os.py/blob/master/LICENSE)

-----------------

<div align="left">

## What is os.py?
**os.py** is a free, open-source Python library which makes retrieving system and hardware information, as well as modifying and manipulating system settings e.g. Windows registry keys much easier.
## Installation
### You can install os.py using pip:
Remember, that os.py is currently in [Private Alpha ❌](https://github.com/Bamboooz/os.py/#roadmap) stage, and the package is not uploaded to pip yet.

```bash
pip install os_py
```

## Usage
### Retrieving System Information
You can use os.py to retrieve system information, such as the firmware type, operating system version, and processor information.

```python
import os_py

# Get the firmware type (BIOS or UEFI)
firmware_type = os_py.sys.get_firmware_type()

# Get the operating system version
os_version = os_py.sys.get_os_version()

# Get the processor model
processor_info = os_py.cpu.get_processor_info()['model']
```

### Working with the Windows Registry
You can use os.py to read from and write to the Windows registry.

```python
import os_py

# Read a value from the registry
value = os_py.registry.read_registry_key(
    os_py.registry.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',
    'Desktop'
)

# Write a value to the registry
os_py.registry.write_registry_key(
    os_py.registry.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',
    'Desktop',
    'C:\\Users\\User\\Desktop'
)
```

### Reading system and hardware data from command prompt.
You can use os.py directly from the command prompt.

```bash
os_py --dump=cmd 
```

You can also dump the os.py information into a .txt file

```bash
os_py --dump=txt --file={specify your filepath}
```

### And many more!
These were just random examples of os.py usage, but there's a lot more to explore, visit [os.py docs](https://github.com/Bamboooz/os.py/wiki) to learn about everything you can do with os.py.

## Roadmap
### Project launch state
> **os.py** launched in **May 2022**. As of **April 2023**, we are in the **Private Alpha** stage ❌.<br/>

❌ **Private Alpha:** os.py is currently being developed, and you cannot install the library yet.<br/>
✅ **Public Alpha:** Anyone can install and use os.py. There may be issues, but we are working to resolve them actively.<br/>
🔶 **Public Beta:** Stable enough for non-enterprise use-cases.<br/>
💻 **Public:** os.py is production ready.

### What's left to do for the library to be published
> [ ] Gathering system and hardware information on Windows
> [x] Using os.py from the command prompt
> [x] Using os.py to modify registry. and other system settings.

### Future ideas
> [ ] os.py logging class
> [ ] Gathering system and hardware information on Linux
> [ ] Support for machines with multiple motherboards, CPU's, GPU's etc.
> [ ] Support for more operating systems. (Linux is first priority)


## Documentation

 * [Documentation](https://github.com/Bamboooz/os.py/wiki)
 * [PyPi page](https://pypi.org/project/os_py/)

## License

This project is licensed under the [BSD-3 Clause License](https://opensource.org/license/bsd-3-clause/).