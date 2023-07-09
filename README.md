<p align="center">
<img alt="os.py logo" width="200"
src="https://github.com/Bamboooz/os.py/blob/master/assets/logo.png?raw=true" />
</p>

<p align="center">
os.py is a free, open-source library which allows retrieving system and hardware information in Python 💻
<br>
Available for Windows and Linux, support for more operating systems soon.
</p>

<div align="center">

-----------------
[**Home**](https://github.com/Bamboooz/os.py)⠀
[**Install**](https://github.com/Bamboooz/os.py#installation)⠀
[**Documentation**](https://github.com/Bamboooz/os.py/wiki)⠀
[**Contributing**](https://github.com/Bamboooz/os.py/blob/master/CONTRIBUTING.md)⠀
[**Download**](https://pypi.org/project/os.py#files)⠀
[**Security**](https://github.com/Bamboooz/os.py/blob/master/SECURITY.md)⠀
-----------------

<div align="left">

## What is os.py?
> yeah uhh, so i work on this project everyday like I enjoy doing it but im like still learning don't expect it to work too soon. like it's not that much left but still yeah thank you for starring my project i guess

os.py exposes system and hardware information in a form of a python library. This allows you to write Python-based code to access low-level operating system and hardware data.

os.py allows retrieval of information such us: cpu, gpu information, statistics, supported features and sensors, ram and swap utilization and features, storage device information, external storage device information, machine peripherals and drivers and much more.

## Installation
### You can install os.py using pip:
```bash
pip install ospylib
```

## Usage
### Retrieving System Information
You can use os.py to retrieve system information, such as the firmware type, operating system version, and processor information.

```python
import ospylib

# Get the firmware type (BIOS or UEFI)
firmware_type = ospylib.firmware().type

# Get the operating system name
os_version = ospylib.system().name

# Get the processor model
processor_info = ospylib.cpu().model
```

### Reading system and hardware data from command prompt.
You can use os.py directly from the command prompt:

```bash
ospylib
```

You can also dump the os.py information into a text file:

```bash
ospylib --file {specify your filepath}
```

### And many more!
These were just random examples of os.py usage, but there's a lot more to explore, visit [os.py docs](https://github.com/Bamboooz/os.py/wiki) to learn about everything you can create with os.py.

## Roadmap
### Project launch state
> **os.py** launched in **May 2022**. As of **July 2023**, we are in the **Private ❌** stage.<br/>

❌ **Private:** os.py is currently being developed, and you cannot install the library yet.<br/>
✅ **Public:** os.py is ready for public use and is receiving regular updates.

## Documentation

 * [Documentation](https://github.com/Bamboooz/os.py/wiki)
 * [PyPi page](https://pypi.org/project/ospylib/)

## Support os.py
You can buy me a coffee if you enjoy my work [Buy me a coffee ☕](https://www.buymeacoffee.com/Bamboooz)

## License

This project is licensed under the [BSD-3 Clause License](https://opensource.org/license/bsd-3-clause/).