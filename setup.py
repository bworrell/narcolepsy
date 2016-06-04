#!/usr/bin/env python
# Copyright (c) 2015 - Bryan Worrell
# For license information, see the LICENSE file
import os
import setuptools

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
VERSION_FILE = os.path.join(BASE_DIR, "narcolepsy", 'version.py')
README_FILE  = os.path.join(BASE_DIR, "README.rst")


def normalize(version):
    return version.split()[-1].strip("\"'")


def get_version():
    with open(VERSION_FILE) as f:
        version = next(line for line in f if line.startswith("__version__"))
        return normalize(version)


with open(README_FILE) as f:
    readme = f.read()


extras_require = {
    'docs': [],
    'test': [
        "nose==1.3.0",
        "tox==1.6.1"
    ],
}

setuptools.setup(
    name='narcolepsy',
    description="Give your application a break.",
    author='Bryan Worrell',
    author_email='bworrell@notmyemail.com',
    url='https://github.com/bworrell',
    version=get_version(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    extras_require=extras_require,
    long_description=readme,
    keywords="narcolepsy sleep timing useless"
)
