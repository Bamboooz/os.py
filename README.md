![pysil](https://github.com/Bamboooz/pysil/blob/master/icon.png?raw=true)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Version](https://img.shields.io/github/package-json/v/:user/:repo?filename=packages%2Fchar-width-table-builder%2Fpackage.json)
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)
![pythonver](https://img.shields.io/pypi/pyversions/:packageName)

# PySil
PySil is simple, but useful python library to gather:
  - system information
  - hardware information
  - network information

# Anouncements
Linux support finnaly done!, you can now download PySil library version 1.8
New features:
  - display information (works both for windows and linux!)
  - working linux support 🎉

# Compatibility 
Windows • Linux

# Future updates
### Future updates for PySil library:

- [ ] MacOS Support
- [ ] more functions
- [ ] fixing ram amount bug
- [ ] fixing virtual network bug
- [ ] fixing code quality + reducing library weight
- [ ] importing pysil library to other languages ( java, c# )

# Installing
Installation using python package installer (pip):
```python
pip install pysil # make sure its pysil version 1.0.5 or above, cause it wont work then
```

# Usage
Commands in PySil library are the same for every single
operating system, and you don't have to change anything
in import etc. - my library will automaticly detect
your operating system and apply correct code for you.

Required python pacakges to run pysil library are in the requirements.txt file.

# Known Bugs
- if you have some sort of virtual network installed ( for example you have vmware installed ),
all network functions will return the virtual netwrok information, not yours.
----------------------------------
- gpu total, used, free memory and gpu temp on linux in returning none or errors.
- ----------------------------------
- total ram memory will return not correct amount, it returns a little bit less than you have ( about 0.7 GB ).

# Notes
1) Some of PySil's library functions require to be run as administrator,
because some of them are using libraries like wmi, so if you are
getting an unexpected error, try running your IDE as administrator,
and restart your script.
----------------------------------
2) Some of PySil's library functions might have an error, and if you are having one
for example function is returning wrong data, or function is just not working
please contact me.
 ----------------------------------
3) Some functions might need few seconds ( depending on your computer specs ) to return the data, because it needs to access
files, read them, get needed data and then return it, so be patient. If it is taking longer than about 8sec then please contact me.
----------------------------------
4) Feel free to contribute, I will appriciate it for sure. If you want to do so, please contact me ( preferably discord )
----------------------------------
5) If you found an error or vurnability of any sort, please report it to me.
----------------------------------
6) Contact details:
  - E-mail: bambusixmc@gmail.com
  - Discord: Bamboooz#8423

# License
-------
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
