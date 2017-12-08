#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from io import open
from setuptools import setup


def read_file(fname, encoding='utf-8'):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding=encoding) as r:
        return r.read()


README = read_file("README.rst")
CHANGES = read_file("CHANGES.rst")
version = read_file("VERSION.txt").strip()

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []
test_deps = [
    'mock;python_version<"3.3"',
    "pytest>=3.1",
    "pytest-cov"
]

install_deps = [ ]

setup(
    name="inbus",
    version=version,
    author="Maarten Los",
    author_email="mlos@gmx.com",
    description=("Simple, UDP-based message bus"),
    long_description="\n\n".join([README, CHANGES]),
    license="BSD 2-Clause license",
    keywords="message bus broker publisher subscriber pub sub",
    url="https://github.com/mlos/inbus",
    download_url="https://github.com/mlos/inbus/tarball/" + version,
    packages=["inbus", "inbus.client", "inbus.server", "inbus.shared", "examples", "doc"],
    install_requires=install_deps,
    setup_requires=pytest_runner,
    tests_require=test_deps,
    extras_require={
        'docs': [
            'sphinx>=1.5.1'
        ],
        'test': test_deps,
        'qa': [
            'flake8',
            'rstcheck'
        ]
    },
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: System :: Networking",
        "Topic :: System :: Distributed Computing",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
)
