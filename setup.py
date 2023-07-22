# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import shutil
import platform

from setuptools import setup


description = 'os.py - Python library as well as command prompt tool to read and manipulate machine information 💻'

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3'
]

keywords = [
    'python', 'windows', 'linux', 'library', 'device', 'cpu',
    'hardware', 'storage', 'gpu', 'display', 'drivers'
    'motherboard', 'system-monitor', 'terminal',
    'hardware-information', 'network-information'
]

packages = ['battery', 'common', 'device', 'display', 'drivers', 'hardware', 'sensors', 'storage', 'system', 'peripherals', 'process', 'audio']

if platform.system() == 'Windows':
    install_requirements = [
        'wmi'
    ]
else:
    install_requirements = []

entry_points = {
    'console_scripts': [
        'ospylib = prompt.__init__:main'
    ]
}


setup(
    name='ospylib',
    version='1.0.0',
    description=description,
    long_description=open('README.txt').read(),
    url='https://github.com/Bamboooz/os.py',
    author='Bamboooz',
    author_email='bambusixmc@gmail.com',
    license='BSD-3-Clause',
    classifiers=classifiers,
    keywords=keywords,
    packages=packages,
    install_requires=install_requirements
)


if __name__ == '__main__':
    # run this file using python setup.py sdist bdist_wheel
    password = input('Enter your pypi password: ')
    api_key = input('Enter your pypi API key: ')
    os.system(f'twine upload --repository-url https://upload.pypi.org/legacy/ --username __token__ --password {api_key} dist/*')

    # remove pypi build directories
    shutil.rmtree(f'{os.getcwd()}\\build')
    shutil.rmtree(f'{os.getcwd()}\\dist')
    shutil.rmtree(f"{os.getcwd()}\\{[d for d in os.listdir('.') if os.path.isdir(d) and 'egg-info' in d][0]}")
