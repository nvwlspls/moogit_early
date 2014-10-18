# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import moogit
version = moogit.__version__

setup(
    name='moogit',
    version=version,
    author='',
    author_email='mremeat@gmail.com',
    packages=[
        'moogit',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['moogit/manage.py'],
)