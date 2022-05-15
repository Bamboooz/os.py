from setuptools import setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3'
]

setup(
    name='pysil',
    version='1.0.8',
    description='system information gathering made simple',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/Bamboooz/pysil',
    author='Bamboooz',
    author_email='bambusixmc@gmail.com',
    license='LGPL-2.1',
    classifiers=classifiers,
    keywords='system',
    packages=['pysil', 'core'],
    install_requires=['']
)
