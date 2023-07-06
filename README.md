<div align="center">

![os.py](https://github.com/Bamboooz/os.py/blob/master/assets/logo.png?raw=true)

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
> yeah uhh, so i work on this project everyday like i enjoy doing it but im like still learning don't expect it to work too soon. like its not that much left but still yeah thank you for starring my project i guess

**os.py** is a free, open-source Python library which makes retrieving system and hardware information much easier.<br/>
**os.py** is also available in command prompt mode, which you can use to print the output to the screen, or save it to a file.

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
firmware_type = ospylib.system.firmware()

# Get the operating system name
os_version = ospylib.system.name()

# Get the processor model
processor_info = ospylib.cpu.model()
```

### Reading system and hardware data from command prompt.
You can use os.py directly from the command prompt.

```bash
ospylib --dump=cmd 
```

You can also dump the os.py information into a .txt file

```bash
ospylib --dump=txt --file={specify your filepath}
```

### And many more!
These were just random examples of os.py usage, but there's a lot more to explore, visit [os.py docs](https://github.com/Bamboooz/os.py/wiki) to learn about everything you can do with os.py.

## Roadmap
### Project launch state
> **os.py** launched in **May 2022**. As of **July 2023**, we are in the **Private Alpha  ❌** stage.<br/>

❌ **Private Alpha:** os.py is currently being developed, and you cannot install the library yet.<br/>
✅ **Public Alpha:** Anyone can install and use os.py. There may be issues, but we are working to resolve them actively.<br/>
🔶 **Public Beta:** Stable enough for non-enterprise use-cases.<br/>
💻 **Public:** os.py is production ready.

## Documentation

 * [Documentation](https://github.com/Bamboooz/os.py/wiki)
 * [PyPi page](https://pypi.org/project/ospylib/)

## Support os.py
You can buy me a coffee if you enjoy my work [Buy me a coffee ☕](https://www.buymeacoffee.com/Bamboooz)

## License

This project is licensed under the [BSD-3 Clause License](https://opensource.org/license/bsd-3-clause/).