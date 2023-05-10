<div align="center">

![os.py](https://github.com/Bamboooz/os.py/assets/blob/master/logo.png?raw=true)

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

# os.py

## What is os.py?
**os.py** is a free, open-source Python library which makes retrieving system and hardware information, as well as modifying and manipulating system settings e.g. Windows registry keys much easier.<br/>
**os.py** is also available in command prompt mode, which you can use to print the output to the screen, or save it to a file.

## Installation
### You can install os.py using pip:
```bash
pip install ospy  # it should be available really really soon, I am having problems with pypi administration.
```

## Usage
### Retrieving System Information
You can use os.py to retrieve system information, such as the firmware type, operating system version, and processor information.

```python
import ospy

# Get the firmware type (BIOS or UEFI)
firmware_type = ospy.machine.get_firmware_type()

# Get the operating system version
os_version = ospy.sys.get_os_info()['version']

# Get the processor model
processor_info = ospy.cpu.get_processor_info()['model']
```

### Reading system and hardware data from command prompt.
You can use os.py directly from the command prompt.

```bash
ospy --dump=cmd 
```

You can also dump the os.py information into a .txt file

```bash
ospy --dump=txt --file={specify your filepath}
```

### And many more!
These were just random examples of os.py usage, but there's a lot more to explore, visit [os.py docs](https://github.com/Bamboooz/os.py/wiki) to learn about everything you can do with os.py.

## Roadmap
### Project launch state
> **os.py** launched in **May 2022**. As of **April 2023**, we are in the **Public Alpha  ✅** stage.<br/>

❌ **Private Alpha:** os.py is currently being developed, and you cannot install the library yet.<br/>
✅ **Public Alpha:** Anyone can install and use os.py. There may be issues, but we are working to resolve them actively.<br/>
🔶 **Public Beta:** Stable enough for non-enterprise use-cases.<br/>
💻 **Public:** os.py is production ready.

### Future ideas
 * [ ] Gathering system and hardware information on Linux
 * [ ] GUI coverage for os.py
 * [ ] modifying os settings using os.py
 * [ ] os.py logging class
 * [ ] Support for machines with multiple motherboards, CPU's etc.
 * [ ] Support for AMD GPU's.
 * [ ] Support for more operating systems. (Linux is first priority)

> You can view the current development status on our [trello page](https://trello.com/b/5rmlwrUg/ospy) as well.

## Documentation

 * [Documentation](https://github.com/Bamboooz/os.py/wiki)
 * [PyPi page](https://pypi.org/project/os_py/)

## Support os.py
You can buy me a coffee if you enjoy my work [Buy me a coffee ☕](https://www.buymeacoffee.com/Bamboooz)

## License

This project is licensed under the [BSD-3 Clause License](https://opensource.org/license/bsd-3-clause/).