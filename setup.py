# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from setuptools import setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3'
]

required_packages = []

setup(
    name='ospy',
    version='0.0.1',
    description='os.py - Python library as well as command prompt tool to read and manipulate machine information 💻',
    long_description=open('README.txt').read(),
    url='https://github.com/Bamboooz/os.py',
    author='Bamboooz',
    author_email='bambusixmc@gmail.com',
    license='BSD-3-Clause',
    classifiers=classifiers,
    entry_points={
        'console_scripts': [
            'ospy.cmd=ospy.cmd.__main__:main'
        ]
    },
    keywords=['python', 'windows', 'library', 'device', 'cpu',
              'hardware', 'storage', 'gpu', 'display',
              'motherboard', 'system-monitor', 'terminal',
              'hardware-information', 'network-information'],
    packages=['ospy', 'ospy/cmd', 'ospy/arch', 'ospy/shared', 'ospy/arch/windows'],
    install_requires=required_packages
)

# os.system('python C:\Users\Bambu\Pulpit\Programowanie\os.py\setup.py sdist bdist_wheel')
# os.system('twine upload --repository-url https://upload.pypi.org/legacy/ dist/*')
