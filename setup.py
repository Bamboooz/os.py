# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import shutil

from setuptools import setup


description = 'os.py - Python library as well as command prompt tool to read and manipulate machine information 💻'

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3'
]

keywords = [
    'python', 'windows', 'library', 'device', 'cpu',
    'hardware', 'storage', 'gpu', 'display',
    'motherboard', 'system-monitor', 'terminal',
    'hardware-information', 'network-information'
]

entry_points = {
    'console_scripts': [
        'ospy.cmd=ospy.cmd.__main__:main'
    ]
}

packages = ['ospy', 'ospy/cmd', 'ospy/arch', 'ospy/shared', 'ospy/arch/windows']


setup(
    name='ospy',
    version='0.0.1',
    description=description,
    long_description=open('README.txt').read(),
    url='https://github.com/Bamboooz/os.py',
    author='Bamboooz',
    author_email='bambusixmc@gmail.com',
    license='BSD-3-Clause',
    classifiers=classifiers,
    entry_points=entry_points,
    keywords=keywords,
    packages=packages
)


if __name__ == '__main__':
    # run this file using python setup.py sdist bdist_wheel
    password = input('Enter your pypi password: ')
    os.system(f'twine upload --repository-url https://upload.pypi.org/legacy/ -u Bamboooz -p {password} dist/*')

    # remove pypi build directories
    shutil.rmtree(f'{os.getcwd()}\\build')
    shutil.rmtree(f'{os.getcwd()}\\dist')
    shutil.rmtree(f"{os.getcwd()}\\{[d for d in os.listdir('.') if os.path.isdir(d) and 'egg-info' in d][0]}")
