#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import platform


if 'Darwin' in platform.system():
    install_requires = ["pyobjc-framework-Quartz==3.1.1"]


setup(
    name = 'python-desktop-recording',
    version = '0.0.1', 
    description = 'screen recording',
    long_description = 'screen recording',
    packages = find_packages(),
    install_requires=install_requires,
    author = 'Tim Hsu',
    url = 'https://github.com/livingbio/desktop-recording',
    author_email = 'tim.yellow@gmail.com',
    license = 'MIT',
    platforms = 'mac',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_data={
        'recording': ['*.scpt'],
        },
)